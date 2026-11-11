
set -e

echo "=================================="
echo "STUDENT PERFORMANCE ANALYTICS"
echo "=================================="

echo ""
echo "Step 1: Running student analysis..."
python main.py

echo ""
echo "Step 2: Running prediction model..."
python predictions.py

echo ""
echo "Project completed successfully!"