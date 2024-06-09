# Pomodoro Timer with Alarm

This Python script implements a simple Pomodoro timer that alternates between work and rest periods, playing an alarm sound at the end of each session. It also includes features to pause and stop the timer.

## Pomodoro Technique

The Pomodoro Technique is a time management method that can help you improve your productivity and focus. Developed by Francesco Cirillo in the late 1980s, it's named after the Italian word for 'tomato', which was the shape of the kitchen timer Cirillo used as a student.

### How It Works

1. **Work Session (Pomodoro):** You work for 25 minutes straight with complete focus on a single task.
2. **Short Break:** After the work session, you take a short break of 5 minutes to relax.
3. **Repeat:** You repeat this process, taking a longer break of 15-30 minutes after every four Pomodoros.

### Benefits

- **Enhanced Focus:** Frequent breaks keep your mind fresh and focused.
- **Prevents Burnout:** Regular breaks ensure you don't get exhausted.
- **Improves Time Management:** Breaking down work into intervals helps manage complex tasks better.
- **Boosts Motivation:** Completing small, manageable chunks of work provides a sense of achievement.

## Features

- **Customizable Work/Rest Intervals**: Set your desired work and rest times in the format HH:MM:SS.
- **Cycle Count**: Specify the number of Pomodoro cycles you want to run.
- **Alarm Sound**: Plays an alarm sound when a work or rest period ends.
- **Pause Functionality**: New feature to pause the work and rest timers.
- **Stop Functionality**: New feature to stop the Pomodoro timer in the middle of a session.

## Executable Version

- The script has been converted into an executable file using PyInstaller with the command `pyinstaller --onefile countdown_timer.py`. This allows for easy distribution and execution without the need for a Python environment.

## Requirements

- Python 3.x
- `winsound` module (Windows only)
- `tqdm` module for progress visualization (optional)

## Usage

1. Run the script in your command line or terminal.
2. Enter the work and rest times when prompted.
3. Enter the number of cycles you wish to complete.
4. The timer will start, and you can follow the on-screen prompts to pause or stop the timer.

## Code Breakdown

The script defines a function `get_seconds` to convert time strings into seconds. The `countdown` function manages the timer, displaying the remaining time and playing an alarm sound at the end. The `cycle` function orchestrates the work and rest periods according to the user's input.

# Future Features
So far the script uses a piano sound for the timer.
Feature will use a music catalog to play music during duration of rest.



## Contributions

Contributions are welcome! If you have suggestions or want to add new features, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.
