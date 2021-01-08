import psutil
import argparse
import logging
from psutil._common import bytes2human


logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: Line - %(lineno)d # %(message)s')


def print_mem_to_human(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def monitoring(show_stats):
    logging.debug("Start getting values")
    if show_stats == "cpu":
        print("CPU: the number of logical CPUs: {}".format(psutil.cpu_count()))
        print("CPU: load over the last 1, 5 and 15 minutes: {}".format(psutil.getloadavg()))
        print("CPU: current frequency: {} Mhz".format(psutil.cpu_freq().current))
        print("CPU: the current system-wide CPU utilization: {} %".format(psutil.cpu_percent(interval=0.5)))

    elif show_stats == "memory":
        print('MEMORY\n------')
        print_mem_to_human(psutil.virtual_memory())
        print('\nSWAP\n----')
        print_mem_to_human(psutil.swap_memory())

    elif show_stats == "disk":
        pass


def parse_args():
    parser = argparse.ArgumentParser(description="Choose which info to show")
    parser.add_argument("--show_stats", choices=["cpu", "memory", "disk"], required=True, dest="show_stats",
                        help="Info require to show, possible variants cpu, memory, disk")
    return parser.parse_args()


def main():
    args = parse_args()
    logging.debug(vars(args))
    monitoring(show_stats=args.show_stats)


if __name__ == '__main__':
    main()
