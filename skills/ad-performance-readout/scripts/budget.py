#!/usr/bin/env python3
"""Budget calculator: weekly budget, ads you can read, and how many to launch.

Usage:
  python3 budget.py --target-cac 100 --monthly 5000
  python3 budget.py --target-cac 100 --weekly 2500 --event-rate 0.25

--event-rate is the share of the optimisation event that becomes a customer,
for example trial-to-paid. It checks whether you can afford 50 events a week.
Uses only the Python standard library.
"""
import argparse
import math


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target-cac", type=float, required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--monthly", type=float)
    g.add_argument("--weekly", type=float)
    p.add_argument("--event-rate", type=float, help="Event to customer rate, such as 0.25 for 25%% trial-to-paid")
    a = p.parse_args()

    cac = a.target_cac
    weekly = a.weekly if a.weekly is not None else a.monthly / 4
    readable = math.floor(weekly / (2 * cac))
    concepts = readable // 6
    launch = concepts * 4

    how = "monthly / 4" if a.weekly is None else "as given"
    print(f"Weekly budget: {weekly:,.0f} ({how})")
    print(f"Read one ad: 2x target CAC = {2 * cac:,.0f}")
    print(f"Prove one winner: 10x target CAC = {10 * cac:,.0f}")
    print(f"Ads you can read this week: {readable}")
    if concepts:
        print(f"Launch: {concepts} concept(s) x 4 versions = {launch} ads on Monday, in a new ad set.")
        print("The rest of the budget funds the ads that earn more spend, up to 5x and then 10x.")
    else:
        print("Launch: under 6 readable ads a week. You cannot read a full brief of 4 versions with room to invest.")
        print(f"Raise the weekly budget to {12 * cac:,.0f} to read 1 concept, or lower the event you optimise for.")

    if a.event_rate:
        per_event = cac * a.event_rate
        events = weekly / per_event
        print(f"\nTarget cost per event: target CAC x event rate = {per_event:,.2f}")
        print(f"Events you can afford a week: {events:,.0f}")
        print(f"Budget for 50 events a week: {50 * per_event:,.0f}")
        if events < 50:
            print("Under 50 a week, Meta is guessing. Optimise for an earlier event you can afford 50 of.")


if __name__ == "__main__":
    main()
