# Arduino Vibration Condition Monitoring System

## Project Overview

This project was designed to monitor vibration data from industrial machinery at Calor Gas Coryton and visualize it in real-time for condition monitoring purposes. The system provides an early warning system for equipment maintenance by detecting abnormal vibration patterns.

## Purpose

Industrial equipment condition monitoring through vibration analysis is crucial for:
- Predictive maintenance scheduling
- Preventing unexpected equipment failures
- Reducing downtime and maintenance costs
- Ensuring operational safety

## Hardware Components

- **Arduino** (microcontroller)
- **SW-120 Vibration Sensor** - Digital vibration detection sensor
- **2 x LEDs** - Visual indication system for vibration status
- **Connecting wires and breadboard**

*Note: The SW-120 sensor is ideal for proof of concept and educational purposes. For industrial applications, more sophisticated accelerometers would be recommended.*

## Software Components

### Arduino Code
- Reads vibration data from SW-120 sensor
- Controls LED indicators based on vibration detection
- Serial communication for data transmission

### Python Data Analysis
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Real-time data visualization and plotting
- Data logging and trend analysis

## System Operation

1. **Detection**: SW-120 sensor continuously monitors for vibrations
2. **Indication**: LEDs provide immediate visual feedback
   - LED status indicates presence/absence of vibration
3. **Data Collection**: Vibration data transmitted via serial communication
4. **Visualization**: Python scripts process and display real-time data trends
5. **Analysis**: Historical data analysis for condition monitoring patterns

## Features

- Real-time vibration monitoring
- Visual LED indication system
- Data logging capabilities
- Graphical data visualization
- Historical trend analysis
- Serial communication interface

## Installation & Setup

### Arduino Setup
1. Connect SW-120 sensor to digital input pin
2. Connect LEDs to digital output pins
3. Upload the Arduino sketch to your board

### Python Environment
```bash
pip install pandas matplotlib pyserial
```

### Running the System
1. Upload Arduino code to your microcontroller
2. Connect Arduino to computer via USB
3. Run Python visualization script
4. Monitor real-time vibration data

## Applications

- **Industrial Equipment Monitoring**: Motors, pumps, compressors
- **Predictive Maintenance**: Early fault detection
- **Educational Projects**: Learning vibration analysis concepts
- **Proof of Concept**: Testing monitoring system designs

## Future Improvements

- Integration with more sensitive accelerometer sensors
- Wireless data transmission capabilities
- Advanced signal processing algorithms
- Database integration for long-term data storage
- Web-based monitoring dashboard
- Alert system notifications

## Project Context

Developed for industrial condition monitoring at Calor Gas Coryton facility. This proof-of-concept demonstrates the feasibility of low-cost vibration monitoring systems for equipment maintenance applications.

## Files Structure

```
├── arduino_code/          # Arduino sketches
├── python_scripts/        # Data visualization scripts
├── data/                 # Logged vibration data
└── documentation/        # Project documentation
```

## Technology Stack

- **Hardware**: Arduino, SW-120 Vibration Sensor
- **Programming**: C++ (Arduino), Python
- **Libraries**: Pandas, Matplotlib
- **Communication**: Serial/USB

## Author

DevRoss-Ops

## License

This project is open source and available for educational and research purposes.

---

*Note: This is a proof-of-concept system. For production industrial applications, consider using industrial-grade sensors and certified monitoring equipment.*