#!/usr/bin/env python3


def contribution_margin_per_unit(unit_price: float, unit_cost: float) -> float:
    """
    Calculate the contribution margin per unit.

    Parameters:
    unit_price: The selling price per unit.
    unit_cost: The variable cost per unit.

    Returns:
    float: The contribution margin per unit.
    """

    return unit_price - unit_cost


def break_even_units(
    contribution_margin_per_unit: float, fixed_costs: float, desired_profit: float = 0
) -> int:
    """
    Calculate the break-even point in units.

    Parameters:
    contribution_margin_per_unit: The contribution margin per unit.
    fixed_costs: The total fixed costs.
    desired_profit: The desired profit (default is 0).
    """

    units = (fixed_costs + desired_profit) / contribution_margin_per_unit

    return int(units) if units.is_integer() else int(units) + 1


def contribution_margin_ratio(
    contribution_margin_per_unit: float, unit_price: float
) -> float:
    """
    Calculate the contribution margin ratio.

    Parameters:
    contribution_margin_per_unit: The contribution margin per unit.
    unit_price: The selling price per unit.

    Returns:
    float: The contribution margin ratio.
    """

    return contribution_margin_per_unit / unit_price


def break_even_sales(
    contribution_margin_ratio: float, fixed_costs: float, desired_profit: float = 0
) -> float:
    """
    Calculate the break-even point in sales dollars.

    Parameters:
    contribution_margin_ratio: The contribution margin ratio.
    fixed_costs: The total fixed costs.
    desired_profit: The desired profit (default is 0).

    Returns:
    float: The break-even point in sales dollars.
    """

    return (fixed_costs + desired_profit) / contribution_margin_ratio


def margin_of_safety(sales: float, break_even_sales: float) -> float:
    """
    Calculate the margin of safety.

    Parameters:
    sales: The actual sales.
    break_even_sales: The break-even sales.

    Returns:
    float: The margin of safety.
    """

    return (sales - break_even_sales) / sales


def print_raw_data(
    unit_price: float, unit_cost: float, fixed_costs: float, desired_profit: float
) -> None:
    print("Raw Data:")
    print(f"\tUnit Price: {unit_price:,.2f}")
    print(f"\tUnit Cost: {unit_cost:,.2f}")
    print(f"\tFixed Costs: {fixed_costs:,.2f}")
    print(f"\tDesired Profit: {desired_profit:,.2f}\n")


def print_sales_volume(break_even_units: int, break_even_sales: float) -> None:
    """
    Print the sales volume in units and dollars.
    """
    print("Sales Volume:")
    print(f"\tUnit Volume: {break_even_units:,}")
    print(f"\tSales Volume: ${break_even_sales:,.2f} dollars\n")


def print_income_statement(
    units_sold: int, unit_price: float, unit_cost: float, fixed_costs: float
) -> None:
    """
    Print the income statement using contribution margin format.
    """
    sales = units_sold * unit_price
    vc = units_sold * unit_cost
    cm = sales - vc
    net_income = cm - fixed_costs

    print("Income Statement (Contribution Margin Format):\n")
    print(f"\tSales: {sales:,.2f}")
    print(f"\tVariable cost: {vc:,.2f}")
    print(f"\tContribution margin: {cm:,.2f}\n")
    print(f"\tFixed cost: {fixed_costs:,.2f}\n")
    print(f"\tNet income: {net_income:,.2f}\n")


def print_margin_of_safety(
    margin_of_safety_units: float,
    margin_of_safety_dollars: float,
    margin_of_safety_ratio: float,
) -> None:
    """
    Print the margin of safety in units, dollars, and ratio.
    """
    print("Margin of Safety:")
    print(f"\tMargin of Safety (Units): {margin_of_safety_units:,}")
    print(f"\tMargin of Safety (Dollars): ${margin_of_safety_dollars:,.2f}")
    print(f"\tMargin of Safety (Ratio): {margin_of_safety_ratio:.2%}\n")


def print_report(
    unit_price: float,
    unit_cost: float,
    fixed_costs: float,
    desired_profit: float = 0,
    units_sold: int = 0,
) -> None:
    """
    Print the report with all the calculated values.
    """
    print("Report: -------------------------------\n")
    print_raw_data(unit_price, unit_cost, fixed_costs, desired_profit)

    # Contribution margin per unit and contribution margin ratio
    cmpu = contribution_margin_per_unit(unit_price, unit_cost)
    cmr = contribution_margin_ratio(cmpu, unit_price)
    print(f"Contribution Margin per Unit: {cmpu:.2f}")
    print(f"Contribution Margin Ratio: {cmr:.2f}\n")

    # Sales volume
    be_units = break_even_units(cmpu, fixed_costs, desired_profit)
    be_sales = break_even_sales(cmr, fixed_costs, desired_profit)
    print_sales_volume(be_units, be_sales)

    # Income statement in contribution margin format
    print_income_statement(be_units, unit_price, unit_cost, fixed_costs)

    # Margin of safety
    if units_sold > 0:
        print(f"Units Sold: {units_sold:,}\n")
        # unit_price = 80
        # unit_cost = 30
        # fixed_costs = 313_600
        # cmpu = contribution_margin_per_unit(unit_price, unit_cost)
        # cmr = contribution_margin_ratio(cmpu, unit_price)
        # be_units = break_even_units(cmpu, fixed_costs, desired_profit)
        # be_sales = break_even_sales(cmr, fixed_costs, desired_profit)

        ms_units = units_sold - be_units
        ms_dollars = ms_units * unit_price
        ms = margin_of_safety(units_sold, be_units)

        print_margin_of_safety(ms_units, ms_dollars, ms)


def part1():
    # Raw data
    unit_price = 87
    unit_cost = 24
    fixed_costs = 441_000
    desired_profit = 0
    units_sold = 0

    # print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)

    desired_profit = 252_000
    # print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)

    unit_price = 80
    # print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)

    fixed_costs = 308_000
    # print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)

    unit_cost = 30
    # print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)

    units_sold = 10_000
    desired_profit = 0
    print_report(unit_price, unit_cost, fixed_costs, desired_profit, units_sold)


def part2():
    # Power Model
    p_unit_price = 780
    p_unit_cost = 490
    p_cmpu = p_unit_price - p_unit_cost
    p_fixed_costs = 13_000
    p_desired_profit = 0
    p_units_sold = 230

    # print_report(p_unit_price, p_unit_cost, p_fixed_costs, p_desired_profit)

    # Lite Model
    l_unit_price = 620
    l_unit_cost = 400
    l_cmpu = l_unit_price - l_unit_cost
    l_fixed_costs = 139_100
    l_desired_profit = 0
    l_units_sold = 920

    # print_report(l_unit_price, l_unit_cost, l_fixed_costs, l_desired_profit)

    total_units_sold = p_units_sold + l_units_sold
    total_fixed_costs = p_fixed_costs + l_fixed_costs

    p_ratio = p_units_sold / total_units_sold
    l_ratio = l_units_sold / total_units_sold

    print(f"Relative percentage for Power: {p_ratio:.2%}")
    print(f"Relative percentage for Lite: {l_ratio:.2%}")

    p_wgt_avg_cmpu = p_cmpu * p_ratio
    l_wgt_avg_cmpu = l_cmpu * l_ratio

    combo_wgt_avg_cmpu = p_wgt_avg_cmpu + l_wgt_avg_cmpu

    print(f"Weighted average contribution margin per unit: {combo_wgt_avg_cmpu:.2f}")

    combo_be_units = break_even_units(combo_wgt_avg_cmpu, total_fixed_costs, 0)
    print(f"Break-even units for the combo: {combo_be_units:,.2f}")

    p_be_units = combo_be_units * p_ratio
    l_be_units = combo_be_units * l_ratio

    print("\nLite and Power break-even units:")
    print(f"\tPower: {p_be_units:,.0f}")
    print(f"\tLite: {l_be_units:,.0f}")

    p_sales = p_be_units * p_unit_price
    l_sales = l_be_units * l_unit_price
    t_sales = p_sales + l_sales

    p_vc = p_be_units * p_unit_cost
    l_vc = l_be_units * l_unit_cost
    t_vc = p_vc + l_vc

    p_cm = p_sales - p_vc
    l_cm = l_sales - l_vc
    t_cm = p_cm + l_cm

    p_net_income = p_cm - p_fixed_costs
    l_net_income = l_cm - l_fixed_costs
    t_net_income = p_net_income + l_net_income

    print(
        f"Sales -\n\tPower: ${p_sales:,.2f}; \tLite: ${l_sales:,.2f}; \tTotal: ${t_sales:,.2f}"
    )
    print(
        f"Variable Costs -\n\tPower: ${p_vc:,.2f}; \tLite: ${l_vc:,.2f}; \tTotal: ${t_vc:,.2f}"
    )
    print(
        f"Contribution Margin -\n\tPower: ${p_cm:,.2f}; \tLite: ${l_cm:,.2f}; \tTotal: ${t_cm:,.2f}"
    )
    print(
        f"Fixed Costs -\n\tPower: ${p_fixed_costs:,.2f}; \tLite: ${l_fixed_costs:,.2f}; \tTotal: ${total_fixed_costs:,.2f}"
    )
    print(
        f"Net Income -\n\tPower: ${p_net_income:,.2f}; \tLite: ${l_net_income:,.2f}; \tTotal: ${t_net_income:,.2f}"
    )

    margin_of_ratio = (total_units_sold - (p_be_units + l_be_units)) / total_units_sold
    print(f"\n\nMargin of Safety Ratio: {margin_of_ratio:.2%}")


def main():
    # part1()
    part2()


main()
