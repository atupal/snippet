/*
 * author: atupal
 * date: 9/14/2013
 * */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv/cv.h>
#include "opencv2/legacy/legacy.hpp"
#include "opencv2/nonfree/features2d.hpp"

#define abs(a, b) (a) < (b) ? (b) - (a) : (a) - (b)

int is_left(IplImage*, IplImage*);
int is_right(IplImage*, IplImage*);
int is_top(IplImage*, IplImage*);
int is_bottom(IplImage*, IplImage*);
IplImage* read_img(int);
int show_img(IplImage *);
IplImage* splice_img_h(IplImage *img1, IplImage *img2);

vector<int> queue;

int find_left(int);

/*
 * the is_direction is means that
 * img2 is on the direction of img
 *
 * */

int is_left(IplImage *img, IplImage *img2) {
  queue.clear();
  int width = img->width;
  int height = img->height;
  int step = img->widthStep;
  uchar *data = (uchar *) img->imageData;
  uchar *data2 = (uchar *) img2->imageData;
  assert(width == img2->width);
  assert(height == img2->height);
  assert(step == img2->widthStep);
  /*
   * detect the row
   * */
  int row_cnt = 0;
  for (int i = 0; i < height; i += 2) {
    int flag = 1;
    int tmp_1 = 0;
    for (int j = 0; j < width; ++ j) {
      int s = 0;
      for (int c = 0; c < 3; ++ c) {
        s += (int)data[i * step + j * 3 + c];
      }
      s /= 3;
      if (s < 125) {
        tmp_1 += 1;
      }
    }
    if (tmp_1 > 5) 
      flag = 0;
    int tmp_2 = 0;
    if (flag) {
      for (int j = 0; j < width; ++ j) {
        int s = 0;
        for (int c = 0; c < 3; ++ c) {
          s += (int)data2[i * step + j * 3 + c];
        }
        s /= 3;
        if (s < 125) {
          tmp_2 += 1;
        }
      }
    }
    if (tmp_2 > 5)
      row_cnt += 1;
  }
  printf("row_cnt:%d\n", row_cnt);

  int cnt = 0;
  for (int i = 0; i < height; ++ i) {
    for (int j = width - 1; j < width; ++ j) {
      int tmp_1 = 0;
      int tmp_2 = 0;
      for (int c = 0; c < 3; ++ c) {
        tmp_1 += data[i * step + j * 3 + c];
        tmp_2 += data2[i * step + (width - 1 - j) * 3 + c];
      }
      tmp_1 /= 3;
      tmp_2 /= 3;
      int gap = abs(tmp_1, tmp_2);
      if (gap > 65) {
        queue.push_back(i);
        ++ cnt;
      }
    }
  }

  printf("cnt:%d\n", cnt);
  //splice_img_h(img, img2);
  //return cnt * 2 + row_cnt;
  return cnt * 1000 + row_cnt;
}

int is_right(IplImage *img1, IplImage *img2) {


  return 1;
}

int is_top(IplImage *img1, IplImage *img2) {


  return 1;
}

int is_bottom(IplImage *img1, IplImage *img2) {


  return 1;
}

int find_left(int ind) {
  IplImage *img = read_img(ind);
  int min = 1000;
  int mark = -1;
  //for (int i = 137; i < 138; ++ i) {
  for (int i = 0; i < 209; ++ i) {
    if (i != ind) {
      int ret = is_left(img, read_img(i));
      if (ret / 1000 < min and ret % 1000 < 5) {
      //if (ret < min) {
        mark = i;
        min = ret / 1000;
        //min = ret;
      }
    }
  }
  if (mark != -1)
    splice_img_h(img, read_img(mark));
  printf("mark:%d\n", mark);
  return 0;
}

IplImage* read_img(int i) {
  char name[256];
  sprintf(name, "%.3d", i);
  char full_name[1024];
  strncpy(full_name, "img/", 5);
  strncat(full_name, name, 1024);
  strncat(full_name, ".bmp", 5);
  IplImage *img = cvLoadImage(full_name);
  printf("read img: %s\n", full_name);

  return img;
}

IplImage* splice_img_h(IplImage *img1, IplImage *img2) {
  assert(img1->height == img2->height);
  int height = img1->height;
  int width1 = img1->width;
  int width2 = img2->width;
  IplImage *img = cvCreateImage(cvSize(width1 + width2 + 1, height), IPL_DEPTH_8U, 3);
  //printf("%d", img->nChannels);
  int step1 = img1->widthStep;
  int step2 = img2->widthStep;
  int step = img->widthStep;
  for (int i = 0; i < height; ++ i) {
    for (int j = 0; j < width1; ++ j) {
      for (int c = 0; c < 3; ++ c) {
        img->imageData[i * step + j * 3 + c] = img1->imageData[i * step1 + j * 3 + c];
      }
      img->imageData[i * step + width1 * 3 + 2] = 255;
    }
    for (int j = 0; j < width2; ++ j) {
      for (int c = 0; c < 3; ++ c) {
        img->imageData[i * step + (width1 + j + 1) * 3 + c] = img2->imageData[i * step2 + j * 3 + c];
      }
    }
  }
  for (int i = 0; i < (int)queue.size(); ++ i) {
    cvCircle(img, cvPoint(width1, queue[i]), 1, cvScalar(0, 255, 0), 1);
  }
  show_img(img);
  return img;
}

int show_img(IplImage *img) {
  cvNamedWindow("win_2");
  cvMoveWindow("win_2", 200, 0);
  cvShowImage("win_2", img);
  cvWaitKey();
  cvDestroyWindow("win_2");
}

int base() {
  printf("main");
  return 0;
}

int ts_read() {
  IplImage *img = read_img(0);
  if (img) {
    printf("height: %d\n", img->height);
    printf("width: %d\n", img->width);
    printf("chnnel: %d\n", img->nChannels);
    int width = img->width;
    int height = img->height;
    int step = img->widthStep;
    uchar *data = (uchar *)img->imageData;
    return 0;
    for (int i = 0; i < height; ++ i) {
      for (int j = 0; j < 1; ++ j) {
        printf("%d ", data[i * step + j]);
      }
      printf("\n");
    }
    //show_img(img);
    return 0;
  }
  return -1;
}

int ts_find_left() {
  for (int i = 0; i < 200; ++ i) {
    find_left(i);
  }
}

int ts() {
  printf("*********************test***********************\n");
  //ts_read();
  ts_find_left();
  return 0;
}

int main() {
  ts();
  //base();
  return 0;
}
