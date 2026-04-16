[y, fs] = audioread('sounds/traffic.mp3'); % Load the file
t = (0:length(y)-1)/fs;           % Create time vector
%plot(t, y);                       % Time-domain plot
subplot(4,2,3)
plot(t,y)
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: traffic');

subplot(4,2,4)
plot(abs(fft(y)))
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: traffic');