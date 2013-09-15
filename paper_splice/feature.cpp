/*
 * atupal
 * */

#include <stdio.h>
#include <iostream>
#include "opencv2/core/core.hpp"
//#include "opencv2/features2d/features2d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/legacy/legacy.hpp"
#include <opencv2/nonfree/features2d.hpp>

using namespace cv;
using namespace std;

void readme();
int cmp(void *, void *);
void on_mouse( int event, int x, int y, int flags, void* param );

std::vector<KeyPoint> keypoints_1, keypoints_2;
int row = 1;
int col = 1;

/** @function main */
int main( int argc, char** argv )
{
    //initModule_nonfree();//THIS LINE IS IMPORTANT 没这个方法嘛
    if( argc != 3 )
    { readme(); return -1; }

    IplImage *img = cvLoadImage("img/test.png");

    cvThreshold(img, img, 70, 255,CV_THRESH_BINARY);
    cvSaveImage("img/test.png", img);

    Mat img_1 = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );
    Mat img_2 = imread( argv[2], CV_LOAD_IMAGE_GRAYSCALE );

    //二值化图片
    //cvThreshold(&img_2, &img_2, 70, 255,CV_THRESH_BINARY);

    if( !img_1.data || !img_2.data )
    { std::cout<< " --(!) Error reading images " << std::endl; return -1; }

    //-- Step 1: Detect the keypoints using SURF Detector
    //int minHessian = 400;
    int minHessian = 30000;

    SurfFeatureDetector detector( minHessian );


    detector.detect( img_1, keypoints_1 );
    detector.detect( img_2, keypoints_2 );

    //-- Draw keypoints
    Mat img_keypoints_1; Mat img_keypoints_2;

    drawKeypoints( img_1, keypoints_1, img_keypoints_1, Scalar::all(-1), DrawMatchesFlags::DEFAULT );
    drawKeypoints( img_2, keypoints_2, img_keypoints_2, Scalar::all(-1), DrawMatchesFlags::DEFAULT );

    for (int i = 0; i < keypoints_1.size(); ++ i) {
        cout << i << ":"<< keypoints_1[i].pt.x << "," << keypoints_1[i].pt.y << endl;
        char t[256];
        sprintf(t, "%d", i);
        putText(img_keypoints_1, t , keypoints_1[i].pt, 
                    FONT_HERSHEY_COMPLEX_SMALL, 0.6, cvScalar(0,0,255), 1, CV_AA);
    }

    //for (int i = 0; i < keypoints_2.size(); ++ i) {
    //    cout << "[" << i << "] "<< keypoints_2[i].pt.x << " " << keypoints_2[i].pt.y << endl;
    //    char t[256];
    //    sprintf(t, "%d", i);
    //    putText(img_keypoints_2, t , keypoints_2[i].pt, 
    //                FONT_HERSHEY_COMPLEX_SMALL, 0.5, cvScalar(0,0,255), 1, CV_AA);
    //}

    

    //-- Show detected (drawn) keypoints
    cvNamedWindow("img");
    IplImage tmp = IplImage(img_keypoints_1);

    /*
    cvCreateTrackbar( "row", "img", &row, 7, NULL );
    cvCreateTrackbar( "col", "img", &col, 7, NULL );
    cvSetMouseCallback("img", on_mouse, 0 );
    */

    for(;waitKey(0) != '\x1b'; ) {
        //imshow("Keypoints 1", img_keypoints_1 );
        cvShowImage("img", &tmp );
        //imshow("Keypoints 2", img_keypoints_2 );

        cvWaitKey(0);
    }
    

    return 0;
}

/** @function readme */
void readme()
{ std::cout << " Usage: ./fe <img1> <img2>" << std::endl; }

int cmp(void *a, void *b) {
    
}

void on_mouse( int event, int x, int y, int flags, void* param )
{
    if (CV_EVENT_LBUTTONDOWN == event) {
        int t = 0;
        double m = 100000000;
        for (int i = 0; i < keypoints_1.size(); ++ i) {
            double mm = pow( (keypoints_1[i].pt.x - x), 2) + pow( (keypoints_1[i].pt.y - y),2 );
            if (mm < m) {
                m = mm;
                t = i;
            }
        }
        if(col <= 19)
            cout << (row - 1) << "," << (col - 1) <<  ":" << t << endl;
        else {
            col = 0;
            row += 1;
        }
        col += 1;

        //if(col < 8 )cout << (row - 1) * 3 + 1 << "," << (col - 1) * 3 + 1 <<  ":" << t << endl;
        //else {
        //    col = 0;
        //    row += 1;
        //}
    }
}
