def write_report(analysis_results, insights, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("T-Shirt Sales Analysis Report\n")
        file.write("============================\n\n")

        file.write(f"Total Revenue: ${analysis_results['total_revenue']:.2f}\n")
        file.write(f"Total T-Shirts Sold: {analysis_results['total_quantity']}\n")
        file.write(f"Average Price per T-Shirt: ${analysis_results['avg_price']:.2f}\n\n")

        file.write("T-Shirt Sizes by Revenue\n")
        file.write("------------------------\n")
        for size, revenue in analysis_results["sorted_sizes"]:
            quantity = analysis_results["size_quantity"].get(size, 0)
            file.write(f"Size {size}: ${revenue:.2f} - {quantity} units\n")

        file.write("\nT-Shirt Colours by Revenue\n")
        file.write("--------------------------\n")
        for color, revenue in analysis_results["sorted_colors"]:
            quantity = analysis_results["color_quantity"].get(color, 0)
            file.write(f"{color}: ${revenue:.2f} - {quantity} units\n")

        file.write("\nT-Shirt Designs by Revenue\n")
        file.write("--------------------------\n")
        for design, revenue in analysis_results["sorted_designs"]:
            file.write(f"{design}: ${revenue:.2f}\n")

        file.write("\nKey Insights\n")
        file.write("------------\n")

        if "top_size_revenue" in insights:
            size, revenue = insights["top_size_revenue"]
            file.write(f"Best size by revenue: {size} (${revenue:.2f})\n")

        if "top_size_quantity" in insights:
            size, quantity = insights["top_size_quantity"]
            file.write(f"Most popular size by quantity: {size} ({quantity} units)\n")

        if "top_color" in insights:
            color, revenue = insights["top_color"]
            file.write(f"Best colour: {color} (${revenue:.2f})\n")

        if "top_design" in insights:
            design, revenue = insights["top_design"]
            file.write(f"Top design: {design} (${revenue:.2f})\n")

def print_summary(analysis_results):
    print("\nT-Shirt Sales Summary")
    print("---------------------")
    print(f"Total Revenue: ${analysis_results['total_revenue']:.2f}")
    print(f"Total Units Sold: {analysis_results['total_quantity']}")
    print(f"Average Price: ${analysis_results['avg_price']:.2f}")

    print("\nTop Sizes:")
    for size, revenue in analysis_results["sorted_sizes"][:3]:
        print(f"{size}: ${revenue:.2f}")

    print("\nTop Colours:")
    for color, revenue in analysis_results["sorted_colors"][:3]:
        print(f"{color}: ${revenue:.2f}")