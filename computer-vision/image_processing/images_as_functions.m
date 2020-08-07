# pkg list;
# pkg load image;

img = imread('dolphin.png');
imshow(img);


% Crop an image
img = imread('bicycle.png');
imshow(img);

disp(size(img));  % check size

cropped = img(110:310, 10:160);
imshow(cropped);

% TODO: Find out cropped image size
disp(size(cropped))

% Color planes
img = imread('fruit.png');
imshow(img);
disp(size(img));

% TODO: Select a color plane, display it, inspect values from a row
img_red = img(:, :, 1);
plot(img_red(150,:));
img_green = img(:, :, 2);
img_blue = img(:, :, 3);

imshow(img_red);

imshow(img_green);

imshow(img_blue);


dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');

average1 =  dolphin / 2 + bicycle / 2;
average2 =  (dolphin + bicycle) / 2;
imshow(average1);
figure, imshow(average2);

subplot(1,2,1), imshow(average1)
subplot(1,2,2), imshow(average2)

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

result = blend(dolphin, bicycle, 0.75);
imshow(result); % note: will result in an error if blend() returns empty or incorrect value

sigma = 100;
im = imread('fruit.png');
noise = randn(size(im)) .* sigma;
output = im + noise;
imshow(output);

% Image processing function imabsdiff
% imabsdiff = (a-b) + (b-a)
pkg load image;
imshow(imabsdiff(dolphin, bicycle));


noise = randn([1 100]);
% x is bin centers, n is count of bin values
[n, x] = hist(noise, [-3 -2 -1 0 1 2 3]);
disp([x; n]);
plot(x, n);

noise = randn([1 10000]);
[n, x] = hist(noise, linspace(-3, 3, 21));
% disp([x; n]);
plot(x, n);

% TODO: Try generating other kinds of random numbers.
height = 3;
width = 4;

% (3,4) matrix of uniform random values between 0.0 to 1.0
x = rand(height, width);
disp(x);

% (3,4) matrix of uniform random values between 0 to 10
y = randi(10, height, width);
disp(y);

% A 2D grid of random Gaussian values
height = 3;
width = 4;
x = randn(height, width);
disp(x);
