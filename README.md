# GOTM Documentation Website

Official documentation for the General Ocean Turbulence Model (GOTM).

**Live Site:** https://gotm-model.github.io/gotm-model-hugo  
**Code Repository:** https://github.com/gotm-model/code

## Quick Start

### Prerequisites
- Hugo v0.146.0+ (Extended version)
- Git

### Running Locally
```bash
# Clone with theme
git clone https://github.com/gotm-model/gotm-model-hugo.git
cd gotm-model-hugo

# Run Hugo
hugo server -D

# Open http://localhost:1313
```

## Updating Documentation

### Single Source Workflow

All documentation comes from one master file:
```
source/GOTM_Complete_Documentation.md  →  [split script]  →  content/docs/
```

**To update:**
1. Edit `source/GOTM_Complete_Documentation.md`
2. Run `python3 source/split_documentation.py`
3. Test with `hugo server -D`
4. Commit and push

### Structure
```
gotm-model-hugo/
├── source/
│   ├── GOTM_Complete_Documentation.md   # Master source
│   └── split_documentation.py           # Splitting script
├── content/
│   ├── docs/                            # Generated content
│   └── about/
├── themes/
│   └── hugo-book/                       # Hugo Book theme
├── config.yaml                          # Hugo configuration
└── .github/workflows/deploy.yml         # Auto-deployment
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Documentation: CC BY 4.0  
GOTM Code: GPL-2.0

## Contact

- Issues: https://github.com/gotm-model/gotm-model-hugo/issues
- Discussions: https://github.com/gotm-model/gotm-model-hugo/discussions
