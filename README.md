# Pomodoro Timer with Alarm

This Python script implements a simple Pomodoro timer that alternates between work and rest periods, playing an alarm sound at the end of each session. It also includes features to pause and stop the timer.

## Features

- **Customizable Work/Rest Intervals**: Set your desired work and rest times in the format HH:MM:SS.
- **Cycle Count**: Specify the number of Pomodoro cycles you want to run.
- **Alarm Sound**: Plays an alarm sound when a work or rest period ends.
- **Pause Functionality**: New feature to pause the work and rest timers.
- **Stop Functionality**: New feature to stop the Pomodoro timer in the middle of a session.

## Requirements

- Python 3.x
- `winsound` module (Windows only)
- `tqdm` module for progress visualization (optional)

## Usage

1. Run the script in your command line or terminal.
2. Enter the work and rest times when prompted.
3. Enter the number of cycles you wish to complete.
4. The timer will start, and you can follow the on-screen prompts to pause or stop the timer.

## How It Works

The script defines a function `get_seconds` to convert time strings into seconds. The `countdown` function manages the timer, displaying the remaining time and playing an alarm sound at the end. The `cycle` function orchestrates the work and rest periods according to the user's input.

## Contributions

Contributions are welcome! If you have suggestions or want to add new features, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.
