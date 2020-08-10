% % pkg list;
% % pkg load image;
% 
% % Gradient Direction
% function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
%     % TODO Find and return pixels that fall within the desired mag, angle range
%     result = gmag >= mag_min & angle_low <= gdir & gdir <= angle_high;
% end
% 
% % pkg load image;
% 
% %% CANNY EDGE OPERATOR
% 
% % 1. Filter image with derivative of Gaussian
% % 2. Find magnitude and orientation of gradient
% % 3. Non-maximum suppression
% %   Thin multi-pixel wide ridges down to single pix width
% % 4. Linking and thresholding 
% %   a. Define 2 thresholds
% %   b. Use high threshold to start edge curves and low threshold to continue them.
% 
% lena = imread('lena.png');
% figure, imshow(lena), title('Original image, color');
% 
% lenaMono = rgb2gray(lena);
% lenaSmooth= imfilter(lenaMono, h);
% 
% %% Method 1: Canny edge detector
% cannyEdges = edge(lenaMono, 'canny');
% figure, imshow(cannyEdges), title('Original edges');
% 
% cannyEdges2 = edge(lenaSmooth, 'canny');
% figure, imshow(cannyEdges2), title('edges of smoothed image');
% 
% %% Method 2: Laplacian of Gaussian
% logEdges = edge(lenaMono, 'log');
% figure, imshow(logEdges), title('Laplacian of Gaussian');

%% LINE FINDING WITH HOUGH ALGORITHM
peak_threshold = 0.6;
peak_nhood_size = [5 5];
line_fill_gap = 50;
line_min_len = 100;
find_lines('shapes.png', peak_threshold, peak_nhood_size, line_fill_gap, line_min_len);

% LINE FINDING function
function hough_rs = find_lines(img_name, peak_thres, peak_nhood_size, line_fill_gap, line_min_len)
    img = imread(img_name);
    grays= rgb2gray(img);
    edges = edge(grays, 'canny');
    
    %     figure, imshow(img), title('Original image, color');
    %     figure, imshow(grays), title('Original image, grayscale');
    %     figure, imshow(edges), title('edge pixes');

    % Apply Hough transform to find candidate lines
    [H, theta, rho] = hough(edges);
    figure, imagesc(H, 'XData', theta, 'YData', rho), title('Hough accumulator'); 

    % peaks = houghpeaks(H, 100); 
    peaks = houghpeaks(H, 100, 'Threshold', ceil(peak_thres * max(H(:))), 'NHoodSize', peak_nhood_size);
    hold on; plot(theta(peaks(:, 2)) , rho(peaks(:, 1)), 'rs'); hold off;

    % lines = houghlines (edges, theta, rho, peaks);
    lines = houghlines (edges, theta, rho, peaks, 'FillGap', line_fill_gap, 'MinLength', line_min_len);
    figure, imshow (img), title('Line sigments');
    hold on;
    for k = 1:length(lines)
        points = [lines(k).point1; lines(k).point2];
        plot (points(:, 1), points(: ,2), 'LineWidth', 2, 'Color', 'green');
    end
    hold off;
    hough_rs = 1;
end
