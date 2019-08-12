#include <opencv2\opencv.hpp> // It's just easier to #include only this
using namespace cv;

int main() {

    // Don't use global variables if they are not needed!
    VideoCapture vid(0); 
    Mat frame;
    while(true)  
    {
        // Read frame
        vid.read(frame);

        // Draw rectangle
        rectangle(frame, Point(100, 100), Point(300, 300), Scalar(255, 0, 0) /*blue*/, 10, 8, 0);
        // Show image
        imshow("Webcam", frame);

        if ((waitKey(30) & 0xFF) == 27) { // for portability
            break;
        }
    }
}
