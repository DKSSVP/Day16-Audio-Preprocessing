
import os
import wave


def inspect_wav_audio_file(file_path):
    """Inspect WAV audio properties and check the 16 kHz standard."""

    if not os.path.isfile(file_path):
        print(f"[ERROR] Audio file not found: {file_path}")
        return

    try:
        with wave.open(file_path, "rb") as wav_file:
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()
            total_frames = wav_file.getnframes()

            duration = total_frames / sample_rate

            print("\n--- Audio File Properties ---")
            print(f"File: {os.path.basename(file_path)}")
            print(
                f"Channels: {channels} "
                f"({'Mono' if channels == 1 else 'Stereo' if channels == 2 else 'Multichannel'})"
            )
            print(f"Sample Width: {sample_width * 8}-bit")
            print(f"Sample Rate: {sample_rate} Hz")
            print(f"Duration: {duration:.2f} seconds")

            if sample_rate != 16000:
                print(
                    "[WARN] Sample rate is not 16000 Hz! "
                    "Resampling is recommended."
                )
            else:
                print("[OK] Sample rate meets the 16 kHz standard.")

    except (wave.Error, EOFError) as error:
        print(f"[ERROR] Unable to read WAV file: {error}")


if __name__ == "__main__":
    print("Audio Preprocessing Module Ready.")

    audio_path = input(
        "\nEnter the path of a WAV file (or press Enter to exit): "
    ).strip().strip('"')

    if audio_path:
        inspect_wav_audio_file(audio_path)
    else:
        print("No audio file supplied. Exiting.")