# Contributing to Structured Reasoning

Thank you for your interest in contributing to the Structured Reasoning skill!

## How to Contribute

### Reporting Issues

If you encounter problems or have suggestions:

1. Check existing issues to avoid duplicates
2. Open a new issue with:
   - Clear description of the problem or suggestion
   - Examples demonstrating the issue
   - Expected vs actual behavior
   - Your environment (Claude Code version, OS)

### Proposing Changes

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Update SKILL.md if changing core functionality
   - Update or add reference documentation
   - Add examples to worked-examples.md if applicable
   - Update README.md if adding features

4. **Test your changes**
   - Test with Claude Code in various scenarios
   - Verify all modes still work correctly
   - Check that documentation is clear

5. **Commit your changes**
   ```bash
   git commit -m "Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what changed and why
   - Reference any related issues
   - Include examples if applicable

## Development Guidelines

### File Structure

```
structured-reasoning/
├── SKILL.md                     # Main skill specification
├── references/
│   ├── light-mode.md           # Light Mode documentation
│   ├── deep-mode.md            # Deep Mode documentation
│   ├── consensus-mode.md       # Consensus Mode documentation
│   ├── mode-selection-guide.md # Decision framework
│   └── worked-examples.md      # Complete walkthroughs
├── README.md                    # Project overview
├── LICENSE                      # MIT License
├── CONTRIBUTING.md             # This file
└── .gitignore                  # Git ignore rules
```

### Documentation Style

- Use clear, concise language
- Include examples for complex concepts
- Use tables for comparisons
- Use code blocks for templates
- Include visual diagrams where helpful (ASCII art is fine)

### Testing Checklist

Before submitting a PR, verify:

- [ ] All reasoning modes work as expected
- [ ] Decision Router correctly categorizes Type 1/2
- [ ] Escalation triggers work properly
- [ ] Examples in documentation are accurate
- [ ] No broken internal links
- [ ] Markdown formatting is correct
- [ ] Changes are backward compatible (or noted)

## Areas for Contribution

We welcome contributions in these areas:

### Documentation
- Improve clarity of existing documentation
- Add more worked examples
- Create visual diagrams
- Translate documentation

### Features
- Additional reasoning modes
- Improved escalation heuristics
- Better confidence calibration
- Integration with external tools

### Examples
- Domain-specific examples (legal, medical, engineering, etc.)
- Edge case demonstrations
- Performance comparisons

### Testing
- Validation scripts
- Quality checks
- Automated testing frameworks

## Code of Conduct

- Be respectful and constructive
- Focus on ideas, not individuals
- Welcome diverse perspectives
- Assume good intent

## Questions?

Open an issue with the "question" label, and we'll help clarify.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
