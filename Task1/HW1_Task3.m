%Bilal Ayakdaş 220316002
close all;
clear all;
clc
% Read Image
img = imread('images/lighthouse.png');

% Show Image
figure;
subplot(2, 2, 1);
imshow(img);
title('RGB Image');

% Convert to gray scale image
gray = rgb2gray(img);

% Show grayscale image
subplot(2, 2, 2);
imshow(gray);
title('Grayscale Image');

% Rotate  45 degree the image
pkg load image;
rotated_img = imrotate(img, 45);


% Show rotated image
subplot(2, 2, 3);
imshow(rotated_img);
title('Rotated Image');

% Draw the grayscale images's histogram
subplot(2, 2, 4);
imhist(gray);
title('Grayscale Image Histogram');
xlabel('Pixel Intensity');
ylabel('Number Of Pixel');

