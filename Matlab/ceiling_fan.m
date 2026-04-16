[y, fs] = audioread('sounds/ceiling fan.mp3'); % Load the file
t = (0:length(y)-1)/fs;           % Create time vector
subplot(4,2,7)
plot(t, y);                       % Time-domain plot
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: fan');

subplot(4,2,8)
plot(abs(fft(y)))
xlabel('Time (s)'); ylabel('Amplitude');
title('Audio Signal: fan');