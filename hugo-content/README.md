# GOTM Hugo Content

This directory contains the GOTM documentation split into Hugo-compatible markdown files.

## Structure

```
hugo-content/
├── docs/
│   ├── _index.md                    # Main documentation homepage
│   ├── getting-started/             # Installation and quick start
│   │   ├── _index.md
│   │   ├── quick-start.md
│   │   ├── installation.md
│   │   └── dependencies.md
│   ├── theory/                      # Physics and mathematics
│   │   ├── _index.md
│   │   ├── governing-equations.md
│   │   ├── air-sea-interaction.md
│   │   ├── equation-of-state.md
│   │   ├── turbulence-introduction.md
│   │   ├── turbulence-models.md
│   │   └── numerical-methods.md
│   ├── user-guide/                  # Using GOTM
│   │   ├── _index.md
│   │   ├── configuration.md
│   │   ├── input-files.md
│   │   └── command-line.md
│   ├── modules/                     # Module documentation
│   │   ├── _index.md
│   │   ├── architecture.md
│   │   ├── meanflow.md
│   │   ├── turbulence.md
│   │   ├── airsea.md
│   │   ├── observations.md
│   │   ├── output.md
│   │   ├── fabm.md
│   │   ├── cvmix.md
│   │   └── stim.md
│   ├── test-cases/                  # Example simulations
│   │   ├── _index.md
│   │   ├── idealized/               # 10 idealized cases
│   │   │   ├── _index.md
│   │   │   ├── couette.md
│   │   │   ├── entrainment.md
│   │   │   └── ... (8 more)
│   │   └── realistic/               # 11 realistic cases
│   │       ├── _index.md
│   │       ├── ows-papa.md
│   │       ├── nns-annual.md
│   │       └── ... (9 more)
│   └── reference/                   # Reference materials
│       ├── _index.md
│       ├── publications.md
│       ├── glossary.md
│       └── troubleshooting.md
└── about/
    └── _index.md                    # About GOTM, history, team

```

## Usage with Hugo

### 1. Install Hugo

```bash
# macOS
brew install hugo

# Linux (snap)
snap install hugo

# Or download from https://gohugo.io/installation/
```

### 2. Create Hugo Site

```bash
# Create new site
hugo new site gotm-site
cd gotm-site

# Add Hugo Book theme
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book
```

### 3. Copy Content

```bash
# Copy this content directory
cp -r /path/to/hugo-content/docs content/
cp -r /path/to/hugo-content/about content/
```

### 4. Configure Hugo

Create `config.yaml`:

```yaml
baseURL: 'https://www.gotm.net'
title: 'GOTM - General Ocean Turbulence Model'
theme: hugo-book

params:
  BookToC: 3
  BookSearch: true
  BookRepo: 'https://github.com/gotm-model'
  BookMath: true
  BookEnableCodeHighlight: true

menu:
  before:
    - name: "Documentation"
      url: "/docs/"
      weight: 1
    - name: "Test Cases"
      url: "/docs/test-cases/"
      weight: 2
  after:
    - name: "GitHub"
      url: "https://github.com/gotm-model/code"
      weight: 10

markup:
  goldmark:
    renderer:
      unsafe: true
  highlight:
    style: monokai
    lineNos: true
```

### 5. Run Local Server

```bash
hugo server -D
```

Open http://localhost:1313

### 6. Build for Production

```bash
hugo --minify
```

Output in `public/` directory.

## File Organization

- Each major section has an `_index.md` for the section homepage
- Individual pages have descriptive names (e.g., `governing-equations.md`)
- Weight parameter controls ordering (lower numbers appear first)
- `bookToc: true` enables table of contents on that page
- `bookCollapseSection: false` keeps section expanded in sidebar

## Adding Images

To add images for test cases:

1. Create `static/images/cases/` directory
2. Add images there
3. Reference in markdown: `![Caption](/images/cases/image.png)`

## Math Equations

Hugo Book supports KaTeX. Use:

```markdown
Inline: $E = mc^2$

Display:
$$
\frac{\partial k}{\partial t} = P + B - \varepsilon
$$
```

## Next Steps

1. Add images to test case pages
2. Add mermaid diagrams where helpful
3. Create news/blog section if desired
4. Set up automated deployment (GitHub Actions)

## Questions?

See the Hugo migration plan document for detailed guidance.
