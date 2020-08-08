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

