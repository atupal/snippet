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
#include <iostream>
#include <fstream>

using namespace std;

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv/cv.h>
#include "opencv2/legacy/legacy.hpp"
#include "opencv2/nonfree/features2d.hpp"

int abs(int a) {
  return a > 0 ? a : -a;
}

int is_left(IplImage*, IplImage*);
int is_right(IplImage*, IplImage*);
int is_top(IplImage*, IplImage*);
int is_bottom(IplImage*, IplImage*);
IplImage* read_img(int);
int show_img(IplImage *);
IplImage* splice_img_h(IplImage *img1, IplImage *img2);
IplImage* splice_img_v(IplImage *img1, IplImage *img2);

vector<int> queue;
vector<int> queue_2;
int DEBUG = 1;
int fst = 0;
int snd = 0;
char key_down = 0;

int biaozhu[210][210];
int biaozhu_good[210][210];
int vis_r[210];
int vis_l[210];
int B=0;
int E=209;

int find_left(int);

/*
 * the is_direction is means that
 * img2 is on the direction of img
 *
 * */

int through_line(IplImage *img, int i) {
  uchar *data = (uchar *) img->imageData;
  int step = img->widthStep;
  int width = img->width;
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
  return tmp_1;
}

int through_col(IplImage *img, int j, int begin, int end) {
  uchar *data = (uchar *) img->imageData;
  int step = img->widthStep;
  int height = img->height;
  int tmp_1 = 0;
  for (int i = begin + 1; i < end; ++ i) {
    int s = 0;
    for (int c = 0; c < 3; ++ c) {
      s += (int)data[i * step + j * 3 + c];
    }
    s /= 3;
    if (s < 125) {
      tmp_1 += 1;
    }
  }
  return tmp_1;
}

int pix_count(IplImage *img, int w_b, int w_e, int h_b, int h_e) {
  uchar *data = (uchar *) img->imageData;
  int step = img->widthStep;
  int tmp_1 = 0;
  for (int i = w_b + 1; i < w_e; ++ i) {
    for (int j = h_b + 1; j < h_e; ++ j) {
      int s = 0;
      for (int c= 0; c < 3; ++ c) {
        s += (int) data[i * step + j + c];
      }
      s /= 3;
      if (s < 125) {
        tmp_1 += 1;
      }
    }
  }
  return tmp_1;
}



int is_left(IplImage *img, IplImage *img2) {
  biaozhu[8][105] = 1;


  queue.clear();
  int width = img->width;
  int height = img->height;
  int step = img->widthStep;
  uchar *data = (uchar *) img->imageData;
  uchar *data2 = (uchar *) img2->imageData;
  assert(width == img2->width);
  assert(height == img2->height);
  assert(step == img2->widthStep);

  vector<int> line_h;
  vector<int> line_v;
  vector<int> line_h_2;
  vector<int> line_v_2;
  for (int i = 0; i < height; ++ i) {
    int begin = 0;
    int end = 0;
    int tmp_1 = through_line(img, i);
    if (tmp_1 < 2) {
      begin = i;
      while (i < height and tmp_1 < 2) {
        ++ i;
        tmp_1 = through_line(img, i);
      }
      if (i - begin > 3) {
        begin = (begin + i) / 2;
      } else {
        begin = 0;
      }
    }
    if (begin)
      line_h.push_back(begin);
  }

  for (int i = 0; i < height; ++ i) {
    int begin = 0;
    int end = 0;
    int tmp_1 = through_line(img2, i);
    if (tmp_1 < 2) {
      begin = i;
      while (i < height and tmp_1 < 2) {
        ++ i;
        tmp_1 = through_line(img2, i);
      }
      if (i - begin > 7) {
        begin = (begin + i) / 2;
      } else {
        begin = 0;
      }
    }
    if (begin)
      line_h_2.push_back(begin);
  }

  if (line_h.size() != line_h_2.size()) {
    //return 1000;
  }

  for (int i = 0; i < line_h.size(); ++ i) {
    if (abs(line_h[i] - line_h_2[i]) > 6) {
      if(DEBUG)printf("%d,%d:%d\n", line_h[i], line_h_2[i], abs(line_h[i] - line_h_2[i]));
      //return 1000;
    }
    //printf("line:%d, %d\n", line_h[i], line_h_2[i]);
    //cvLine(img, cvPoint(0, line_h[i]), cvPoint(width - 1, line_h[i]), cvScalar(0, 255, 0), 1);
    //cvLine(img2, cvPoint(0, line_h_2[i]), cvPoint(width - 1, line_h_2[i]), cvScalar(0, 255, 0), 1);
    //for (int j = 0; j < width; ++ j) {
    //  int tmp_1 = through_col( img, j, line_h[i],  i + 1 == line_h.size() ? height - 1 : line_h[i + 1]   );
    //  if (tmp_1 < 2) {
    //    int begin = j;
    //    while (j < width and tmp_1 < 2) {
    //      ++ j;
    //      tmp_1 = through_col( img, j, line_h[i],  i + 1 == line_h.size() ? height - 1 : line_h[i + 1]   );
    //    }
    //    begin = (begin + i) / 2;
    //    cvLine(img, cvPoint(begin, line_h[i]), cvPoint(begin, i + 1 == line_h.size() ? height - 1 : line_h[i + 1]), cvScalar(0, 255, 0), 1);
    //  }
    //}
  }


  /*
   * 检测匹配图像两边像素的多少
   * */
  int count_left = 0;
  int count_right = 0;
  for (int x = 0;  x < line_h.size() - 1; ++ x) {
    for (int i = width - 1; i > 0; -- i) {
      int begin = 0;
      int tmp_1 = through_col(img, i, line_h[x], line_h[x + 1]);
      if (tmp_1 < 2) {
        begin = i;
        while (i > 0 and tmp_1 < 2) {
          -- i;
          tmp_1 = through_col(img, i, line_h[x], line_h[x + 1]);
        }
        if (begin - i > 3) {
          begin = (begin + i) / 2;
          //cvLine(img, cvPoint(begin, line_h[x]), cvPoint(begin, line_h[x+1]), cvScalar(0, 255, 0), 1);
          //count_left = pix_count(img, line_h[x], line_h[x+1], begin, width);
          count_left = width - begin;
          if(DEBUG)printf("count_lfet:%d\n", count_left);
          break;
        }
      }
    }

    for (int i = 0; i < width; ++ i) {
      int begin = 0;
      int tmp_1 = through_col(img2, i, line_h[x], line_h[x + 1]);
      if (tmp_1 < 2) {
        begin = i;
        while (i < width and tmp_1 < 2) {
          ++ i;
          tmp_1 = through_col(img2, i, line_h[x], line_h[x + 1]);
        }
        if (i - begin > 3) {
          begin = (begin + i) / 2;
          //cvLine(img2, cvPoint(begin, line_h[x]), cvPoint(begin, line_h[x+1]), cvScalar(0, 255, 0), 1);
          //count_right = pix_count(img2, line_h[x], line_h[x+1], -1, begin);
          count_right = begin;
          if(DEBUG)printf("count_right:%d\n", count_right);
          break;
        }
      }
    }

    if (count_left + count_right > 60 or count_left + count_right < 15) {
      //printf("l_r:%d\n", count_left + count_right);
      //return 1000;
    }

  }

  /*
   * detect the row
   * */
  int row_cnt = 0;
  for (int i = 0; i < height; i += 1) {
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
  //printf("row_cnt:%d\n", row_cnt);

  int cnt = 0;
  int xx[] = {0};
  int yy[] = {0};
  //int xx[] = {-1, 0, 1};
  //int yy[] = {0, 0, 0};
  //int xx[] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
  //int yy[] = {0, 0, 0, -1, -1, -1, 1, 1, 1};
  //int xx[] = {0, 0, 0};
  //int yy[] = {-1, 0, 1};
  int size = 9;
  for (int i = 0; i < height; ++ i) {
    for (int j = width - 1; j < width; ++ j) {
      int tmp_1 = 0;
      int tmp_2 = 0;
      int cnt_tmp_1 = 0;
      int cnt_tmp_2 = 0;
      for (int c = 0; c < 3; ++ c) {
        //tmp_1 += data[i * step + j * 3 + c];
        //tmp_2 += data2[i * step + (width - 1 - j) * 3 + c];
        //
        /*
         * make a Gauss operator to avode random salt.... 233333, :(
         * */
        for (int k = 0; k < size; ++ k) {
          int x = i + xx[k];
          int y = j + yy[k];
          int y2 = (width - 1 - j) + yy[k];
          if ( x > -1 and x < height and y > -1 and y < width) {
            tmp_1 += data[x * step + y * 3 + c];
            cnt_tmp_1 += 1;
          }
          if ( x > -1 and x < height and y2 > -1 and y2 < width) {
            tmp_2 += data2[x * step + y2 * 3 + c];
            cnt_tmp_2 += 1;
          }
        }
      }
      tmp_1 /= cnt_tmp_1;
      tmp_2 /= cnt_tmp_2;
      int gap = abs(tmp_1- tmp_2);
      if (gap > 125) {
        queue.push_back(i);
        ++ cnt;
      }
    }
  }

  //printf("cnt:%d\n", cnt);
  //splice_img_h(img, img2);
  return cnt + row_cnt * 3;
  return cnt + row_cnt;
  return cnt * 2 + row_cnt;
  return cnt * 1000 + row_cnt;
}

int is_right(IplImage *img, IplImage *img2) {

  return 1;
}

int is_top(IplImage *img, IplImage *img2) {
  queue_2.clear();
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
  int col_cnt = 0;
  for (int i = 0; i < width; i += 2) {
    int flag = 1;
    int tmp_1 = 0;
    for (int j = 0; j < height; ++ j) {
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
      for (int j = 0; j < height; ++ j) {
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
      col_cnt += 1;
  }
  //printf("col_cnt:%d\n", col_cnt);
   * */

  int cnt = 0;
  for (int i = 0; i < width; ++ i) {
    for (int j = height - 1; j < height; ++ j) {
      int tmp_1 = 0;
      int tmp_2 = 0;
      for (int c = 0; c < 3; ++ c) {
        tmp_1 += data[j * step + i * 3 + c];
        tmp_2 += data2[(height - 1 - j) * step + i * 3 + c];
      }
      tmp_1 /= 3;
      tmp_2 /= 3;
      int gap = abs(tmp_1- tmp_2);
      if (gap > 65) {
        queue_2.push_back(i);
        ++ cnt;
      }
    }
  }

  //printf("cnt:%d\n", cnt);
  //splice_img_h(img, img2);
  return cnt;
  //return cnt + col_cnt;
}

int is_bottom(IplImage *img1, IplImage *img2) {


  return 1;
}

int find_one_left(int ind) {
  IplImage *img = read_img(ind);
  IplImage *mark_img;
  int old = -1;
  for (int i = 0; i < 209; ++ i) {
    if(vis_r[i]) continue;
  //for (int i = 137; i < 138; ++ i) {
    if (i != ind) {
      mark_img = read_img(i);

      /*detect*/
      int row_cnt = 0;
      int height = img->height;
      int width = img->width;
      int step = img->widthStep;
      uchar *data = (uchar*) img->imageData;
      uchar *data2 = (uchar*) mark_img->imageData;
      for (int z = 0; z < height; z += 1) {
        int flag = 1;
        int tmp_1 = 0;
        for (int j = 0; j < width; ++ j) {
          int s = 0;
          for (int c = 0; c < 3; ++ c) {
            s += (int)data[z * step + j * 3 + c];
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
              s += (int)data2[z * step + j * 3 + c];
            }
            s /= 3;
            if (s < 125) {
              tmp_2 += 1;
            }
          }
        }
        if (tmp_2 > 5)
          row_cnt += 1;
      } /*end detect*/
      if (row_cnt > 2000000) continue;

      splice_img_h(img, mark_img);
      if (key_down == 'r') { 
        printf("%d %d\n", ind, i);
        vis_l[ind] = 1;
        vis_r[i] = i;
        return 0;
      } else if (key_down == 'u') {
        if (old != -1)i = old - 1;
      } else if (key_down == 'd') {
        break;
      }; 
      old = i;
    }
  }
  return -1;
}

int find_one_right(int ind) {
  IplImage *img = read_img(ind);
  IplImage *mark_img;
  int old = -1;
  for (int i = 0; i < 209; ++ i) {
    if(vis_l[i]) continue;
  //for (int i = 137; i < 138; ++ i) {
    if (i != ind) {
      mark_img = read_img(i);

      splice_img_h(img, mark_img);
      if (key_down == 'r') { 
        printf("%d %d\n", ind, i);
        vis_l[ind] = 1;
        vis_r[i] = i;
        return 0;
      } else if (key_down == 'u') {
        if (old != -1)i = old - 1;
      } else if (key_down == 'd') {
        break;
      }; 
      old = i;
    }
  }
  return -1;
}
int find_one_top(int ind) {
  IplImage *img = read_img(ind);
  IplImage *mark_img;
  int old = -1;
  for (int i = 0; i < 11; ++ i) {
    if (i != ind) {
      mark_img = read_img(i);

      splice_img_v(img, mark_img);
      if (key_down == 'r') { 
        printf("%d %d\n", ind, i);
        vis_l[ind] = 1;
        vis_r[i] = i;
        return 0;
      } else if (key_down == 'u') {
        if (old != -1)i = old - 1;
      } else if (key_down == 'd') {
        break;
      }; 
      old = i;
    }
  }
  return -1;
}

int find_left(int ind) {
  IplImage *img = read_img(ind);
  IplImage *mark_img;
  int min = 1000;
  int mark = -1;
  for (int i = 0; i < 209; ++ i) {
    if(vis_r[i]) continue;
  //for (int i = 137; i < 138; ++ i) {
    if (biaozhu_good[ind][i]) {
      mark = i;
      break;
    }
    if (i != ind and not biaozhu[ind][i]) {
      IplImage *img2 = read_img(i);
      int ret = is_left(img, img2);
      //if (ret / 1000 < min and ret % 1000 < 5) {
      if (ret < min) {
        mark = i;
        mark_img = img2;
        //min = ret / 1000;
        min = ret;
      }
    }
  }
  if (mark != -1) {
    vector<int> line_h;
    vector<int> line_v;
    vector<int> line_h_2;
    vector<int> line_v_2;
    int height = img->height;
    int width = img->width;
    if (DEBUG) for (int i = 0; i < height; ++ i) {
      int begin = 0;
      int end = 0;
      int tmp_1 = through_line(img, i);
      if (tmp_1 < 2) {
        begin = i;
        while (i < height and tmp_1 < 2) {
          ++ i;
          tmp_1 = through_line(img, i);
        }
        if (i - begin > 3) {
          begin = (begin + i) / 2;
        } else {
          begin = 0;
        }
      }
      if (begin)
        line_h.push_back(begin);
    }

    if(DEBUG) for (int i = 0; i < height; ++ i) {
      int begin = 0;
      int end = 0;
      int tmp_1 = through_line(mark_img, i);
      if (tmp_1 < 2) {
        begin = i;
        while (i < height and tmp_1 < 2) {
          ++ i;
          tmp_1 = through_line(mark_img, i);
        }
        if (i - begin > 3) {
          begin = (begin + i) / 2;
        } else {
          begin = 0;
        }
      }
      if (begin)
        line_h_2.push_back(begin);
    }

    if(DEBUG)for (int i = 0; i < line_h.size(); ++ i) {
      if (DEBUG)printf("line:%d, %d\n", line_h[i], line_h_2[i]);
      cvLine(img, cvPoint(0, line_h[i]), cvPoint(width - 1, line_h[i]), cvScalar(0, 255, 0), 1);
      cvLine(mark_img, cvPoint(0, line_h_2[i]), cvPoint(width - 1, line_h_2[i]), cvScalar(0, 255, 0), 1);
    }

    if (DEBUG)for (int x = 0;  x < line_h.size() - 1; ++ x) {
      for (int i = width - 1; i > 0; -- i) {
        int begin = 0;
        int tmp_1 = through_col(img, i, line_h[x], line_h[x + 1]);
        if (tmp_1 < 2) {
          begin = i;
          while (i > 0 and tmp_1 < 2) {
            -- i;
            tmp_1 = through_col(img, i, line_h[x], line_h[x + 1]);
          }
          if (begin - i > 3) {
            begin = (begin + i) / 2;
            cvLine(img, cvPoint(begin, line_h[x]), cvPoint(begin, line_h[x+1]), cvScalar(0, 255, 0), 1);
            int count_left = pix_count(img, line_h[x], line_h[x+1], begin, img->width);
            if(DEBUG)printf("count_left:%d\n", width - begin);
            break;
          }
        }
      }
    }

    if(DEBUG)for (int x = 0;  x < line_h.size() - 1; ++ x) {
      for (int i = 0; i < width; ++ i) {
        int begin = 0;
        int tmp_1 = through_col(mark_img, i, line_h[x], line_h[x + 1]);
        if (tmp_1 < 2) {
          begin = i;
          while (i < width and tmp_1 < 2) {
            ++ i;
            tmp_1 = through_col(mark_img, i, line_h[x], line_h[x + 1]);
          }
          if (i - begin > 3) {
            begin = (begin + i) / 2;
            cvLine(mark_img, cvPoint(begin, line_h[x]), cvPoint(begin, line_h[x+1]), cvScalar(0, 255, 0), 1);
            int count_right = pix_count(mark_img, line_h[x], line_h[x+1], -1, begin);
            if(DEBUG)printf("count_right:%d\n", begin);
            break;
          }
        }
      }
    }


    if(DEBUG) printf("mark:%d,%d\n",ind, mark);
    fst = ind;
    snd = mark;
    splice_img_h(img, mark_img);
    return mark;
  } else {
    return 0;
  }
}

int find_right(int ind) {
  IplImage *img = read_img(ind);
  int min = 1000;
  int mark = -1;
  for (int i = 0; i < 209; ++ i) {
  //for (int i = 0; i < 209; ++ i) {
    if (i != ind) {
      int ret = is_left(read_img(i), img);
      //if (ret / 1000 < min and ret % 1000 < 5) {
      if (ret < min) {
        mark = i;
        //min = ret / 1000;
        min = ret;
      }
    }
  }
  if (mark != -1) {
    splice_img_h(img, read_img(mark));
    if (DEBUG)printf("mark:%d\n", mark);
    return mark;
  } else {
    return 0;
  }
}

int find_top(int ind) {
  IplImage *img;// = read_img(ind);
  int min = 1000;
  int mark = -1;
  for (int i = 0; i < 209; ++ i) {
    img = read_img(ind);
    if (i != ind) {
      int ret = is_top(img, read_img(i));
      if (ret < min) {
        mark = i;
        min = ret;
      }
    }
  }
  if (mark != -1 and mark != 1) {
    fst = ind;
    snd = mark;
    splice_img_h(img, read_img(mark));
    if(DEBUG)printf("mark:%d\n", mark);
    return mark;
  } else {
    return 0;
  }
}

IplImage* read_img(int i) {
  char name[256];
  sprintf(name, "%.3d", i);
  char full_name[1024];
  //strncpy(full_name, "img/", 5);
  strncpy(full_name, "img/", 5);
  strncat(full_name, name, 1024);
  strncat(full_name, ".bmp", 5);
  IplImage *img = cvLoadImage(full_name);
  //printf("read img: %s\n", full_name);

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
  char name[256];
  sprintf(name, "ret/%d-%d-h.bmp", fst, snd);
  cvSaveImage(name, img);
  if(DEBUG)for (int i = 0; i < (int)queue.size(); ++ i) {
    cvCircle(img, cvPoint(width1, queue[i]), 1, cvScalar(0, 255, 0), 1);
  }
  show_img(img);
  return img;
}

IplImage* splice_img_v(IplImage *img1, IplImage *img2) {
  assert(img1->width == img2->width);
  int height1 = img1->height;
  int height2 = img2->height;
  int width = img1->width;
  IplImage *img = cvCreateImage(cvSize(width, height1 + height2 + 1), IPL_DEPTH_8U, 3);
  //printf("%d", img->nChannels);
  int step1 = img1->widthStep;
  int step2 = img2->widthStep;
  int step = img->widthStep;
  for (int j = 0; j < width; ++ j) {
    for (int i = 0; i < height1; ++ i) {
      for (int c = 0; c < 3; ++ c) {
        img->imageData[i * step + j * 3 + c] = img1->imageData[i * step1 + j * 3 + c];
      }
      img->imageData[height1 * step + j * 3 + 2] = 255;
    }
    for (int i = 0; i < height2; ++ i) {
      for (int c = 0; c < 3; ++ c) {
        img->imageData[(i + height1 + 1) * step + j * 3 + c] = img2->imageData[i * step2 + j * 3 + c];
      }
    }
  }
  char name[256];
  sprintf(name, "ret/%d-%d-v.bmp", fst, snd);
  cvSaveImage(name, img);
  if (DEBUG)for (int i = 0; i < (int)queue_2.size(); ++ i) {
    cvCircle(img, cvPoint(queue_2[i], height1), 1, cvScalar(0, 255, 0), 1);
  }
  show_img(img);
  return img;
}

int show_img(IplImage *img) {
  cvNamedWindow("win_1");
  cvShowImage("win_1", img);
  while(1) {
    char c = cvWaitKey(0);
    if (c == 81) {
      key_down = 'l';
      break;
    } else if (c == 83){
      key_down = 'r';
      break;
    } else if (c == 82){
      key_down = 'u';
      break;
    } else if (c == 84) {
      key_down = 'd';
      break;
    }
  }
  cvDestroyWindow("win_1");
}

int base() {
  DEBUG=0;
  for (int i = 0; i < 11; ++ i) {
    find_one_top(i);
  }
  return 0;
  for (int i = B; i < E; ++ i) {
    if (vis_l[i]) continue;
    //int left = find_left(i);
    //if (key_down == 'r')printf("%d %d\n", i, left);
    int left = find_one_left(i);

    //int right = find_right(i);
    //printf("%d:%d,%d\n", i, left, right);
  }
  return 0;

  for (int i = B; i < E; ++i) {
    int left = find_top(i);
    printf("%d %d\n", i, left);
  }
  
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
  int now, old;
  now = old = 34;
  for (int i = B; i < E; ++ i) {
    now = find_left(i);
    old = now;
  }
}

int ts_find_top() {
  int now, old;
  now = old = 34;
  for (int i = 0; i < 200; ++ i) {
    now = find_top(i);
    old = now;
  }
}

int ts() {
  printf("*********************test***********************\n");
  //ts_read();
  ts_find_left();
  //ts_find_top();
  return 0;
}

int prepro(){
  ifstream fi;
  fi.open("c_result.raw");
  int l, r;
  while (fi >> l >> r) {
    vis_r[r] = 1;
    vis_l[l] = 1;
    biaozhu_good[l][r] = 1;
  }

  fi.close();
}

int main() {
  //prepro();
  ts();
  //base();
  return 0;
}
