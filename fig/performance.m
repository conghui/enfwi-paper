clc;clear;close all

fwi = ones(1, 40) * 40;
essfwi = ones(1, 40);
enfwi = [1:40];
n = 40;

im2 = plot([1:n], fwi, '-s', ...
    [1:n], essfwi, '-s',  ...
    [1:n], enfwi, '-s', ...
    'MarkerSize', 4, 'Linewidth', 2);

%set(gca, 'XTick', [1:8]);
%set(gca,'xticklabel','Iterations');
axis([0 41 0 41]) 
grid minor
h_legend = legend('FWI', 'ESSFWI',  'ENFWI', 'Location', 'best');
xlabel('Model Samples');
ylabel('Computational Cost (Normalized)');
%text(3.7, 6,'DMA\_get', 'FontSize', 16, 'FontName', 'TimesNewRoman', 'FontAngle','italic')
set(gca, 'FontAngle','italic');
set(gca, 'FontSize', 13);
set(findall( 0, 'FontName', 'Helvetica' ), 'FontName', 'TimesNewRoman' )
