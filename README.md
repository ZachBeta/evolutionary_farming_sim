# Evolutionary Farming Simulator

A 2D/3D hybrid simulation game where players cultivate and guide the evolution of plant life in a dynamic ecosystem.

## Features

- **Evolving Plant Life**: Guide the evolution of plants with unique genetic traits
- **Ecosystem Simulation**: Experience emergent behaviors and symbiotic relationships
- **Dual Perspectives**: Switch between 2D strategy view and 3D first-person interaction
- **Dynamic Environment**: Day/night cycles, weather patterns, and seasonal changes

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd evolutionary-farming-sim
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Simulation

```bash
python -m evolutionary_farming_sim.main
```

## Project Structure

```
evolutionary_farming_sim/
├── core/               # Core game logic and components
├── simulation/         # Simulation systems (plants, environment, etc.)
├── visualization/      # 2D and 3D rendering code
├── config/             # Configuration files
└── assets/             # Game assets (sprites, models, etc.)
    ├── sprites/       # 2D sprite assets
    ├── models/         # 3D model assets
    └── fonts/          # Font files
```

## Development

### Code Style

We use `black` for code formatting and `flake8` for linting:

```bash
black .
flake8
```

### Testing

Run tests using `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
