# pkg list;
# pkg load image;

img = imread('dolphin.jpg');
imshow(img);


% Crop an image
img = imread('bicycle.png');
imshow(img);

disp(size(img));  % check size

cropped = img(110:310, 10:160);
imshow(cropped);

% TODO: Find out cropped image size
