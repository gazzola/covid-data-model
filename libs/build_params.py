f'''
Constants to use for a build. In a separate file to avoid
auto-importing a dataset when we don't necessarily need to.
'''

from datetime import datetime, timedelta, date
from libs.projectected_r_values import projected_intervention_for_state

def get_interventions(state, start_date=datetime.now().date()):
    interventions = [
        None,  # No Intervention
        {  # Flatten the Curve
            start_date: 1.3,
            start_date + timedelta(days=30) : 1.1,
            start_date + timedelta(days=60) : 0.8,
            start_date + timedelta(days=90) : None
        },
        {  # Full Containment
            start_date : 1.3,
            start_date + timedelta(days=7) : 0.3,
            start_date + timedelta(days=30 + 7) : 0.2,
            start_date + timedelta(days=30 + 2*7) : 0.1,
            start_date + timedelta(days=30 + 3*7) : 0.035,
            start_date + timedelta(days=30 + 4*7) : 0
        },
        {  # Social Distancing
            start_date: 1.7,
            start_date + timedelta(days=90) : None
        },
    ]

    projected_intervention = projected_intervention_for_state[state]
    print(projected_intervention)
    interventions.append({
        start_date: projected_intervention['now'],
        start_date + timedelta(days=7) : projected_intervention['nextWeek'],
        start_date + timedelta(days=14) : projected_intervention['inTwoWeeks'],
        start_date + timedelta(days=90) : None
    })

    return interventions


OUTPUT_DIR = 'results/test'