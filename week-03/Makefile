.PHONY: all pdf clean help

# Variables
LATEX_FILE = week-3-project-assignment-costco-slide-deck.tex
PDF_NAME = week-3-project-assignment-costco-slide-deck.pdf
BUILD_DIR = build
PDFLATEX = pdflatex
PDFLATEX_FLAGS = -interaction=nonstopmode -output-directory=$(BUILD_DIR)

# Default target
all: pdf

# Build the PDF
pdf: $(BUILD_DIR)
	@echo "Building PDF..."
	@$(PDFLATEX) $(PDFLATEX_FLAGS) $(LATEX_FILE) > /dev/null 2>&1
	@$(PDFLATEX) $(PDFLATEX_FLAGS) $(LATEX_FILE) > /dev/null 2>&1
	@echo "✓ PDF created: $(BUILD_DIR)/$(PDF_NAME)"

# Create build directory
$(BUILD_DIR):
	@mkdir -p $(BUILD_DIR)

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(BUILD_DIR)
	@rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.bak *.out
	@echo "✓ Clean complete"

# Help
help:
	@echo "Available targets:"
	@echo "  make pdf    - Compile LaTeX and generate PDF in build/ directory"
	@echo "  make clean  - Remove build directory and auxiliary files"
	@echo "  make help   - Display this help message"
