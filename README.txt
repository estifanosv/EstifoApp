
# Book App

This is a Kivy-based mobile app for Android and iPhone that includes:
- Login and Registration
- Book Reading
- Audio Playback (placeholder)
- Q&A Section
- 3-Day Trial Management
- Payment Request Screen

## How to Run

1. Install Kivy:
   pip install kivy

2. Navigate to the app directory:
   cd book_app

3. Run the app:
   python main.py

## How to Publish

### Android
1. Install Buildozer:
   pip install buildozer
   buildozer init

2. Edit buildozer.spec file.

3. Build APK:
   buildozer -v android debug

### iOS
1. Use Kivy-iOS and Xcode on macOS:
   pip install kivy-ios
   toolchain build python3 kivy
   toolchain create BookApp /path/to/app

2. Open the generated Xcode project and run.

## Notes
- Audio playback is a placeholder.
- Payment integration requires backend setup (e.g., Stripe with Flask).
