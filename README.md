# X1-NVM-open_IPs

## Neuromorphic and ReRAM NVM Projects

A curated collection of GitHub projects that apply neuromorphic or ReRAM-based non-volatile memory (NVM) in innovative ways.

## Table of Contents
- [Overview](#overview)
- [Neuromorphic Computing](#neuromorphic-computing)
- [ReRAM Technology](#reram-technology)
- [Featured Projects](#featured-projects)
- [Key Concepts](#key-concepts)
- [Applications](#applications)
- [Resources](#resources)
- [Contributing](#contributing)

## Overview

This repository serves as a comprehensive resource for open-source intellectual property (IPs) and projects related to:
- **Neuromorphic Computing**: Brain-inspired computing architectures that mimic biological neural networks
- **ReRAM (Resistive Random Access Memory)**: Non-volatile memory technology with analog computing capabilities

These technologies enable energy-efficient AI/ML acceleration, in-memory computing, and brain-inspired computing paradigms.

## Neuromorphic Computing

Neuromorphic computing implements neural networks in hardware using principles inspired by biological neural systems. Key characteristics include:

- **Spike-based Processing**: Communication via discrete events (spikes) rather than continuous values
- **Asynchronous Operation**: Event-driven processing without global clocks
- **Co-located Memory and Compute**: Reduces von Neumann bottleneck
- **Energy Efficiency**: Orders of magnitude lower power consumption compared to traditional architectures

### Neuromorphic Hardware Approaches
1. **Digital Neuromorphic**: IBM TrueNorth, Intel Loihi
2. **Analog/Mixed-Signal**: BrainScaleS, SpiNNaker
3. **Memristor-based**: Crossbar arrays with ReRAM devices

## ReRAM Technology

Resistive Random Access Memory (ReRAM) is a non-volatile memory technology that changes resistance based on applied voltage. It offers:

- **Non-volatility**: Retains data without power
- **Analog States**: Multiple resistance levels for multi-bit storage
- **In-Memory Computing**: Perform computations within memory arrays
- **High Density**: Aggressive scaling potential
- **Low Power**: Minimal write energy compared to Flash

### ReRAM Applications
- Analog matrix-vector multiplication for neural networks
- Synaptic weight storage in neuromorphic systems
- Non-volatile configuration memory
- Edge AI accelerators

## Featured Projects

### Neuromorphic Frameworks & Simulators
- **[Brian2](https://github.com/brian-team/brian2)**: Simulator for spiking neural networks in Python
- **[BindsNET](https://github.com/BindsNET/bindsnet)**: Spiking neural network library built on PyTorch
- **[Norse](https://github.com/norse/norse)**: Deep learning library for spiking neural networks in PyTorch
- **[Nengo](https://github.com/nengo/nengo)**: Framework for building, testing, and deploying neural networks
- **[SpykeTorch](https://github.com/miladmozafari/SpykeTorch)**: Spiking neural network simulator based on PyTorch
- **[GeNN](https://github.com/genn-team/genn)**: GPU-enhanced neuronal network simulation framework
- **[NEST Simulator](https://github.com/nest/nest-simulator)**: Simulator for large-scale spiking neural network models
- **[PyNN](https://github.com/NeuralEnsemble/PyNN)**: Language for building neuronal network models

### Hardware Description & RTL
- **[SNNs-STDP-Verilog](https://github.com/snow4060/SNNs-STDP-Verilog)**: Verilog implementation of spiking neural networks with STDP
- **[OpenSpike](https://github.com/sfox14/OpenSpike)**: Open-source neuromorphic computing platform
- **[Neuromorphic Processors](https://github.com/georgia-tech-synergy-lab/Neuromorphic-Processors)**: Hardware implementations and simulators

### ReRAM & Memristor Simulation
- **[MNSIM](https://github.com/thu-nics/MNSIM)**: Neuromorphic architecture simulator with ReRAM crossbar support
- **[DNN+NeuroSim](https://github.com/neurosim/DNN_NeuroSim_V1.0)**: Benchmark of synaptic devices and neural architectures
- **[NeuroSim](https://github.com/neurosim/MLP_NeuroSim_V1.0)**: Circuit-level benchmark for memristor-based computing
- **[PytorchNeuroSim](https://github.com/neurosim/MLP_NeuroSim_V3.0)**: PyTorch-based framework for ReRAM/NVM-based DNN accelerators
- **[MRAM Simulator](https://github.com/MegaSoC/MRAM-Simulator)**: Memory architecture simulator for emerging NVM

### NVM-based Computing Frameworks
- **[CrossSim](https://github.com/sandialabs/cross-sim)**: Cross-point array simulator for analog computing
- **[PANTHER](https://github.com/peaclab/PANTHER)**: Performance modeling tool for ReRAM-based accelerators
- **[NVM-Express](https://github.com/nvmexpress/nvme-cli)**: NVM command line tools and utilities

### Learning Algorithms
- **[SLAYER](https://github.com/bamsumit/slayer)**: Spike layer error reassignment for training deep spiking networks
- **[PySNN](https://github.com/BasBuller/PySNN)**: Efficient spiking neural network library in Python
- **[snnTorch](https://github.com/jeshraghian/snntorch)**: Deep and online learning with spiking neural networks

### Neuromorphic Robotics & Applications
- **[DVS-Gesture](https://github.com/IBMResearch/dvsgesture-dataset)**: Gesture recognition with event cameras
- **[N-MNIST](https://github.com/gorchard/N-MNIST)**: Neuromorphic version of MNIST dataset
- **[Tonic](https://github.com/neuromorphs/tonic)**: Event-based dataset and transformation library

## Key Concepts

### Spiking Neural Networks (SNNs)
- **Leaky Integrate-and-Fire (LIF)**: Basic neuron model with leak current
- **Spike-Timing-Dependent Plasticity (STDP)**: Hebbian learning rule based on spike timing
- **Event-Driven Processing**: Computation triggered by spike events

### Crossbar Arrays
- Passive or active crossbar architectures
- Analog matrix-vector multiplication
- Read/write circuitry and peripheral circuits
- Non-ideal effects: IR drop, sneak path, device variations

### In-Memory Computing
- Computing performed within memory arrays
- Eliminates data movement bottleneck
- Analog computation with digital interface
- Trade-offs between accuracy and efficiency

## Applications

### AI/ML Acceleration
- Energy-efficient edge AI inference
- Real-time pattern recognition
- Low-latency neural network inference

### Autonomous Systems
- Event-based vision processing
- Sensor fusion and decision making
- Adaptive control systems

### Edge Computing
- IoT devices with on-device intelligence
- Battery-powered smart sensors
- Privacy-preserving local processing

### Scientific Computing
- Optimization problems
- Differential equation solving
- Graph analytics

## Resources

### Academic Papers & Conferences
- IEEE International Symposium on Circuits and Systems (ISCAS)
- International Symposium on Low Power Electronics and Design (ISLPED)
- Design, Automation & Test in Europe (DATE)
- International Conference on Neuromorphic Systems (ICONS)

### Research Groups
- Stanford Murmann Group (Mixed-Signal Circuits)
- MIT Neural Networks Group
- IBM Research Neuromorphic Computing
- Intel Labs Neuromorphic Computing Lab

### Datasets
- N-MNIST: Neuromorphic MNIST
- DVS Gesture: Event-based gesture recognition
- N-Caltech101: Neuromorphic object recognition
- CIFAR10-DVS: Event camera version of CIFAR-10

### Tools & Simulators
- Brian2: Python-based SNN simulator
- NEST: Large-scale neural network simulator
- Nengo: Neural engineering framework
- PyTorch: With spiking extensions (Norse, snnTorch)

## Contributing

We welcome contributions to this repository! To add a project or resource:

1. Fork this repository
2. Add your project with description and link
3. Ensure the project is open-source and relevant to neuromorphic/ReRAM NVM
4. Submit a pull request with a clear description

### Contribution Guidelines
- Projects must be publicly accessible on GitHub
- Include a brief description of the project's purpose
- Indicate the technology focus (neuromorphic, ReRAM, or both)
- Verify links are working before submission

## License

This repository is a curated collection of links to external projects. Each linked project has its own license. Please refer to individual project repositories for their specific licensing terms.

---

**Maintained by**: BMsemi  
**Last Updated**: October 2025

For questions or suggestions, please open an issue on this repository.