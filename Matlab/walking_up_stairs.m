[y, fs] = audioread('sounds/walking up stairs.mp3'); % Load the file
t = (0:length(y)-1)/fs;           % Create time vector
subplot(4,2,5)
plot(t, y);                       % Time-domain plot
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: Walking');

subplot(4,2,6)
plot(abs(fft(y)))
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: Stairds');