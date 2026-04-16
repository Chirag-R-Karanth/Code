[y, fs] = audioread('sounds/running.mp3'); % Load the file
t = (0:length(y)-1)/fs;           % Create time vector
subplot(4,2,1);
plot(t, y);                       % Time-domain plot
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: running');

subplot(4,2,2)
plot(abs(fft(y)))
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: running');