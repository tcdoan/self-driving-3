pkg install -forge general control signal image;

pkg list;
img = imread('test.jpg');
imshow(img);

pkg load image;
gray = rgb2gray(img);
imshow(gray);
