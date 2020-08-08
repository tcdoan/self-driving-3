# pkg list;
# pkg load image;

img = imread('dolphin.png');
imshow(img);

% FUNCTIONS: 
function result = scale(img, value)
  result = value .* img;
endfunction
dolphin = imread('dolphin.png');
imshow(scale(dolphin, 1.5));

% Blend two images
function output = blend(a, b, alpha)
    output = alpha*a + (1-alpha)*b;
endfunction

% Test code:
dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');


hsize = 17;
sigma = 5;
h = fspecial('gaussian', hsize, sigma);

surf(h);
imagesc(h);
outim = imfilter(bicycle , h);
imshow(outim);

% Remove noise with a Gaussian filter
im = imread('saturn.png');
imshow(im);

%% Add some noise
noise_sigma = 25;
noise = randn(size(im)) .* noise_sigma;
noisy_im = im + noise;
imshow(noisy_im);

%% Create a Gaussian filter
filter_size = 11;
filter_sigma = 2;

pkg load image;
ksize = 11;
sigma = 2;

filter = fspecial('gaussian', ksize, sigma);
smoothed = imfilter(noisy_im, filter);

subplot(1,2,1), imshow(noisy_im);
subplot(1,2,2), imshow(smoothed);


%% Load an image
img = imread('fall-leaves.png');  % also available: peppers.png, mandrill.png
imshow(img);

ksize = 21;
sigma = 3;
filter = fspecial('gaussian', ksize, sigma);

% smoothed = imfilter(img, filter, 'replicate');
smoothed = imfilter(img, filter, 'symmetric');
subplot(1,2,1), imshow(img);
subplot(1,2,2), imshow(smoothed);



% Apply a median filter
pkg load image;

%% Read an image
img = imread('moon.png');  % also try: brooklyn-bridge.png, penny-farthing.png
imshow(img);

%% TODO: Add salt & pepper noise
noisy_im = imnoise(img, 'salt & pepper', 0.02);

%% TODO: Apply a median filter (how is the result different compared to Gaussian smoothing?)
median_filter = medfilt2(noisy_im);
subplot(1,2,1), imshow(noisy_im );
subplot(1,2,2), imshow(median_filter);


% Find template 1D
% NOTE: Function definition must be the very first piece of code here!
function index = find_template_1D(t, s)
  % TODO: Locate template t in signal s and return index
  % NOTE: Turn off all output from inside the function before submitting!
  c = normxcorr2(t, s);
  %disp([1:size(c,2); c]);
  [maxValue rawIndex] = max(c);
  index = rawIndex - size(t, 2) + 1; 
endfunction

pkg load image; % AFTER function definition

% Test code:
s = [-1 0 0 1 1 1 0 -1 -1 0 1 0 0 -1];
t = [1 1 0];
disp('Signal:'), disp([1:size(s, 2); s]);
disp('Template:'), disp([1:size(t, 2); t]);

index = find_template_1D(t, s);
disp('Index:'), disp(index);


% Find template 2D
% NOTE: Function definition must be the very first piece of code here!
function [yIndex xIndex] = find_template_2D(template, img)
    % TODO: Find template in img and return [y x] location
    % NOTE: Turn off all output from inside the function before submitting!
    c = normxcorr2(template, img);
    [yRaw xRaw] = find(c == max(c(:)));
    yIndex = yRaw - size(template, 1) + 1;
    xIndex = xRaw - size(template, 2) + 1;    
endfunction

pkg load image; % AFTER function definition

% Test code:
tablet = imread('tablet.png');
imshow(tablet);
glyph = tablet(75:165, 150:185);
imshow(glyph);

imshow(tablet);
[y x] = find_template_2D(glyph, tablet);
disp([y x]); % should be the top-left corner of template in tablet
hold on;
plot(x, y, 'r+', 'markersize', 16);
