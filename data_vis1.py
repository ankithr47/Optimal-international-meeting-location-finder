import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def plot_timeline_actual_dates(office_events):
    fig, ax = plt.subplots(figsize=(12, 2.5 + len(office_events)*0.5))
    colors = {"fly_out": "#1565c0", "fly_in": "#1565c0", "meeting": "#388e3c", "wait": "#fbc02d"}

    y_labels = []
    for i, event in enumerate(office_events):
        y_pos = i
        y_labels.append(f"{event['office']} ({event['count']})")
        bar_height = 0.4 + 0.1 * event['count']
        for activity in event["activities"]:
            start_dt = datetime.fromisoformat(activity["start"])
            end_dt   = datetime.fromisoformat(activity["end"])
            ax.barh(y_pos, end_dt - start_dt, left=start_dt, height=bar_height,
                    color=colors[activity["type"]], edgecolor='black')
            ax.text(start_dt + (end_dt - start_dt)/2, y_pos, activity["label"],
                    va='center', ha='center', color='white', fontsize=8, weight='bold')

    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels)
    ax.set_xlabel("Date and Time (UTC)")
    ax.set_title("Timeline of Attendee Journeys by Office (Gantt Style)")

    # Format x-axis for dates and times
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Major ticks every 2 hours
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))  # Date and time format
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()

#office_events = []

"""
office_events = [
    {
        "office": "London",
        "count": 3,
        "activities": [
            {"label": "Outbound Flight", "type": "fly_out", "start": "2026-05-14T05:15", "end": "2026-05-14T09:45"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T09:45", "end": "2026-05-14T11:00"},
            {"label": "Meeting",         "type": "meeting", "start": "2026-05-14T11:00", "end": "2026-05-14T16:00"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T16:00", "end": "2026-05-14T16:40"},
            {"label": "Inbound Flight",  "type": "fly_in",  "start": "2026-05-14T16:40", "end": "2026-05-14T21:10"},
        ]
    },
    {
        "office": "New York",
        "count": 4,
        "activities": [
            {"label": "Outbound Flight", "type": "fly_out", "start": "2026-05-14T01:30", "end": "2026-05-14T10:15"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T10:15", "end": "2026-05-14T11:00"},
            {"label": "Meeting",         "type": "meeting", "start": "2026-05-14T11:00", "end": "2026-05-14T16:00"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T16:00", "end": "2026-05-14T17:00"},
            {"label": "Inbound Flight",  "type": "fly_in",  "start": "2026-05-14T17:00", "end": "2026-05-15T02:00"},  # Overnight flight!
        ]
    },
    {
        "office": "Singapore",
        "count": 2,
        "activities": [
            {"label": "Outbound Flight", "type": "fly_out", "start": "2026-05-14T06:50", "end": "2026-05-14T10:30"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T10:30", "end": "2026-05-14T11:00"},
            {"label": "Meeting",         "type": "meeting", "start": "2026-05-14T11:00", "end": "2026-05-14T16:00"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T16:00", "end": "2026-05-14T17:35"},
            {"label": "Inbound Flight",  "type": "fly_in",  "start": "2026-05-14T17:35", "end": "2026-05-14T22:15"},
        ]
    },
    {
        "office": "Paris",
        "count": 1,
        "activities": [
            {"label": "Outbound Flight", "type": "fly_out", "start": "2026-05-14T07:00", "end": "2026-05-14T10:40"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T10:40", "end": "2026-05-14T11:00"},
            {"label": "Meeting",         "type": "meeting", "start": "2026-05-14T11:00", "end": "2026-05-14T16:00"},
            {"label": "Wait",            "type": "wait",    "start": "2026-05-14T16:00", "end": "2026-05-14T16:15"},
            {"label": "Inbound Flight",  "type": "fly_in",  "start": "2026-05-14T16:15", "end": "2026-05-14T20:56"},
        ]
    }
]
"""
plot_timeline_actual_dates(office_events)
