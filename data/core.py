#!/usr/bin/env python3

COMPLETE_DATA_LEN = 22

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

class SerialInterpreter:
    global g_metric_list

# TODO Fix to right 
    @staticmethod
    def read_metrics(raw_data):
        data_list = raw_data.strip().split(',')
        data_length = len(data_list)
        # Ignore incomplete line of data
        if data_length != COMPLETE_DATA_LEN:
            return
        # Parse data
        g_metric_list['time'].new_value(safe_cast((data_list[0] if 0 < data_length else None), float))
        # g_metric_list['prog'].new_value(safe_cast((data_list[1] if 1 < data_length else None), float))
        # g_metric_list['fracCPAP'].new_value(safe_cast((data_list[2] if 2 < data_length else None), float))
        # g_metric_list['fracPEEP'].new_value(safe_cast((data_list[3] if 3 < data_length else None), float))
        # g_metric_list['fracDual'].new_value(safe_cast((data_list[4] if 4 < data_length else None), float))
        # measured instantaneous oxygen volume fraction [0 to 1.0]
        g_metric_list['v_o2'].new_value(safe_cast((data_list[5] if 5 < data_length else None), float))
        # current instantaneous pressure [cm H2O]
        g_metric_list['v_p'].new_value(safe_cast((data_list[6] if 6 < data_length else None), float))
        # current instantaneous flow to patient [l/min]
        g_metric_list['v_q'].new_value(safe_cast((data_list[7] if 7 < data_length else None), float))
        # highest pressure during inspiration phase of last breath [cm H2o]
        g_metric_list['v_ipp'].new_value(safe_cast((data_list[8] if 8 < data_length else None), float))
        # lowest pressure during inspiration phase of last breath [cm H2O]
        g_metric_list['v_ipl'].new_value(safe_cast((data_list[9] if 9 < data_length else None), float))
        # inspiration time during last breath [ms]
        g_metric_list['v_it'].new_value(safe_cast((data_list[10] if 10 < data_length else None), int))
        # highest pressure during expiration phase of last breath [cm H2o]
        g_metric_list['v_epp'].new_value(safe_cast((data_list[11] if 11 < data_length else None), float))
        # lowest pressure during expiration phase of last breath [cm H2O]
        g_metric_list['v_epl'].new_value(safe_cast((data_list[12] if 12 < data_length else None), float))
        # expiration time during last breath [ms]
        g_metric_list['v_et'].new_value(safe_cast((data_list[13] if 13 < data_length else None), int))
        # BPM for last breath
        g_metric_list['v_bpm'].new_value(safe_cast((data_list[14] if 14 < data_length else None), float))
        # inspiration volume of last breath [ml]
        g_metric_list['v_v'].new_value(safe_cast((data_list[15] if 15 < data_length else None), float))
        # volume per minute averaged over recent breaths [l / min]
        g_metric_list['v_mv'].new_value(safe_cast((data_list[16] if 16 < data_length else None), float))
        # TODO: make use of alarms sent in through serial
        # g_metric_list['v_alarm'].new_value(safe_cast((data_list[17] if 17 < data_length else None), int)
        # set to 0 when between phases, 1 for inspiration phase, -1 for expiration phase
        g_metric_list['v_ie'].new_value(safe_cast((data_list[18] if 18 < data_length else None), int))
        # Highest pressure during any phase of last breath
        g_metric_list['v_pp'].new_value(safe_cast((data_list[19] if 19 < data_length else None), float))
        # Lowest pressure during any phase of last breath
        g_metric_list['v_pl'].new_value(safe_cast((data_list[20] if 20 < data_length else None), float))
        # Measured battery voltage. Over 13v for powered, over 12v for charge remaining
        # g_metric_list['v_batv'].new_value(safe_cast((data_list[21] if 21 < data_length else None), float))

    @staticmethod
    def send_expiratory_pressure():
        print("Sending Expiratory Pressure")
        return "E" + str(g_metric_list['v_pl'].alarms['p_eph'].bound_upper) + "," + str(g_metric_list['v_pl'].alarms['p_epl'].bound_lower) + "," + str(g_metric_list['p_eplTol'].desired_value)

    @staticmethod
    def send_inspiratory_pressure():
        print("Sending Inspiratory Pressure")
        return "I" + str(g_metric_list['v_pp'].alarms['p_iph'].bound_upper) + "," + str(g_metric_list['v_pp'].alarms['p_ipl'].bound_lower) + "," + str(g_metric_list['p_iphTol'].desired_value)

    @staticmethod
    def send_start_operating():
        print("Starting")
        return "R"

    @staticmethod
    def send_timing():
        return "t" + str(g_metric_list['p_it'].desired_value) + "," + str(g_metric_list['p_et'].desired_value)

    @staticmethod
    def send_trigger_type():
        # TODO: is p_it saved as an int or as a boolean
        if safe_cast(g_metric_list['p_trigEnabled'].desired_value, int):
            return "T1"
        else:
            return "T-1"
        
    @staticmethod
    def send_stop_operating():
        print("Stopping")
        return "X"
