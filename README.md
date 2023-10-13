
---
# snake_nest

The snake_nest is a Python script that simplifies the organization of penetration tests. It automatically creates a folder structure tailored for effective information management during a penetration testing engagement.

### Features

- Generates a comprehensive directory structure with designated folders for different types of information.
- Supports easy customization for specific company or machine targets.

### Usage

1. Install Python on your system.
2. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/ChristianJavierS/snake_nest.git
   ```

3. Navigate to the project directory.

   ```bash
   cd snake_nest
   ```

4. Run the script, providing the target company or machine name as an argument.

   ```bash
   python snake_nest.py -n "TargetName"
   ```

### Example

Suppose you're conducting a penetration test for TargetX. Running the script with the argument `-n "TargetX"` will generate the following folder structure:

```
- TargetX
    - EPT (External Penetration Test)
        - evidence
            - credentials
            - data
            - screenshots
        - logs
        - scans
        - scope
        - tools
    - IPT (Internal Penetration Test)
        - evidence
            - credentials
            - data
            - screenshots
        - logs
        - scans
        - scope
        - tools
```

### Installation

Ensure you have Python installed. You can download it [here](https://www.python.org/downloads/).

### Contributing

If you'd like to contribute to this project, please follow the [contributing guidelines](CONTRIBUTING.md).

### License

This project is licensed under the [MIT License](LICENSE).

### Issues and Feedback

Please report any issues or provide feedback on [GitHub Issues](https://github.com/ChristianJavierS/snake_nest/issues).

### Changelog

View the project's changelog [here](CHANGELOG.md).

### Acknowledgments

- Special thanks to Christian for their contributions.

---
