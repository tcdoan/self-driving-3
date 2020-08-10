# pkg list;
# pkg load image;

% Gradient Direction
function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
    % TODO Find and return pixels that fall within the desired mag, angle range
    result = gmag >= mag_min & angle_low <= gdir & gdir <= angle_high;
endfunction

pkg load image;

%% Load and convert image to double type, range [0, 1] for convenience

img = double(imread('octagon.png')) / 255.; 

imshow(img); % assumes [0, 1] range for double images

%% Compute x, y gradients
[gx gy] = imgradientxy(img, 'sobel'); % Note: gx, gy are not normalized

%% Obtain gradient magnitude and direction
[gmag gdir] = imgradient(gx, gy);

imshow(gmag / (4 * sqrt(2))); % mag = sqrt(gx^2 + gy^2), so [0, (4 * sqrt(2))]
imshow((gdir + 180.0) / 360.0); % angle in degrees [-180, 180]

%% Find pixels with desired gradient direction
%% 45 +/- 15
my_grad = select_gdir(gmag, gdir, 1, 30, 60); 
imshow(my_grad);  

%% CANNY EDGE OPERATOR

% 1. Filter image with derivative of Gaussian
% 2. Find magnitude and orientation of gradient
% 3. Non-maximum suppression
%   Thin multi-pixel wide ridges down to single pix width
% 4. Linking and thresholding 
%   a. Define 2 thresholds
%   b. Use high threshold to start edge curves and low threshold to continue them.



% For Your Eyes Only
pkg load image;
imshow(frizzy);
imshow(froomer);
imshow(gray1);
imshow(gray2);



% TODO: Find edges in frizzy and froomer images
frizzy = imread('frizzy.png');
froomer = imread('froomer.png');

gray1 = rgb2gray(frizzy);
gray2 = rgb2gray(froomer);

edges1 = edge(gray1, 'canny');
edges2 = edge(gray2, 'canny');
figure, imshow(edges1);
figure, imshow(edges2);


% edge demo
lena = imread('lena.png');
figure, imshow(lena), title('Original image, color');

lenaMono = rgb2gray(lena);
figure, imshow(lenaMono), title('Original image, monochrome');

%% Make a blurred/smoothed version
h = fspecial('gaussian', [11 11], 4);
disp(h);
figure, surf(h);

lenaSmooth= imfilter(lenaMono, h);
figure, imshow(lenaSmooth), title('Smooth image');

%% Method 1: Shift left and right, and show diff image
lenaL = lenaSmooth;
lenaL(:, [1:(end-1)]) = lenaL(:, [2:end]);

lenaR = lenaSmooth;
lenaR(:, [2:(end)]) = lenaR(:, [1:(end-1)]);
lenaDiff = double(lenaR) - double(lenaL);
figure, imshow(lenaDiff, []), title('Diff between right and left shifted images');

%% Method 2: Canny edge detector
cannyEdges = edge(lenaMono, 'canny');
figure, imshow(cannyEdges), title('Original edges');

cannyEdges = edge(lenaMono, 'canny');
figure, imshow(cannyEdges), title('Original edges');

cannyEdges2 = edge(lenaSmooth, 'canny');
figure, imshow(cannyEdges2), title('edges of smoothed image');

%% Method 3: Laplacian of Gaussian
logEdges = edge(lenaMono, 'log');
figure, imshow(logEdges), title('Laplacian of Gaussian');
