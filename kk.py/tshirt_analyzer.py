from collections import defaultdict

def analyze_tshirts(data):
    size_sales = defaultdict(float)
    color_sales = defaultdict(float)
    design_sales = defaultdict(float)
    size_quantity = defaultdict(int)
    color_quantity = defaultdict(int)

    total_revenue = 0
    total_quantity = 0

    for row in data:
        try:
            amount = float(row.get("amount", 0))
            quantity = int(row.get("quantity", 1))

            size = row.get("size", "Unknown").upper()
            color = row.get("color", "Unknown").title()
            design = row.get("design", "Unknown")

            total_revenue += amount
            total_quantity += quantity

            size_sales[size] += amount
            size_quantity[size] += quantity

            color_sales[color] += amount
            color_quantity[color] += quantity

            design_sales[design] += amount

        except ValueError:
            print(f"Skipping invalid row: {row}")

    avg_price = total_revenue / total_quantity if total_quantity > 0 else 0

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "avg_price": avg_price,
        "sorted_sizes": sorted(size_sales.items(), key=lambda x: x[1], reverse=True),
        "sorted_colors": sorted(color_sales.items(), key=lambda x: x[1], reverse=True),
        "sorted_designs": sorted(design_sales.items(), key=lambda x: x[1], reverse=True),
        "size_quantity": dict(size_quantity),
        "color_quantity": dict(color_quantity),
    }

def generate_insights(analysis_results):
    insights = {}

    if analysis_results["sorted_sizes"]:
        insights["top_size_revenue"] = analysis_results["sorted_sizes"][0]

    if analysis_results["size_quantity"]:
        insights["top_size_quantity"] = max(
            analysis_results["size_quantity"].items(),
            key=lambda x: x[1]
        )

    if analysis_results["sorted_colors"]:
        insights["top_color"] = analysis_results["sorted_colors"][0]

    if analysis_results["sorted_designs"]:
        insights["top_design"] = analysis_results["sorted_designs"][0]

    return insights