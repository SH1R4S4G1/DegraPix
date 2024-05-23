
# DegraPix

DegraPix is a powerful image degradation tool designed to intentionally apply various visual artifacts to images. This application allows users to experiment with different levels of image quality degradation, which can be used for artistic purposes, testing image processing algorithms, or just for fun.

## Features

- **JPEG Compression**: Apply varying levels of compression to degrade image quality.
- **Resize with Restoration**: Scale down the image and then restore it to its original size, repeatedly, to introduce blurring and detail loss.
- **Noise Addition**: Introduce random noise into the image data to simulate data corruption or transmission errors.

## Usage

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/DegraPix.git
   ```
2. **Navigate into the repository directory**:
   ```
   cd DegraPix
   ```
3. **Run the application**:
   ```
   python degradepix.py
   ```
   Follow the on-screen prompts to choose the degradation effects and their parameters.

## Requirements

- Python 3.x
- Pillow library

## Installation

Install the required Python package Pillow, if it's not already installed:

```
pip install Pillow
```

## Contributing

Contributions to DegraPix are welcome! Whether it's bug fixes, new features, or improvements to the documentation, feel free to fork the repository and submit a pull request.

## License

DegraPix is open source software [licensed as MIT](LICENSE).
