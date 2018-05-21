import psutil


# ======================== #
# Colors Used for Printing #
# ======================== #

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# ===================================== #
# Utility Functions (Pretty bar making) #
# ===================================== #

def pretty_bar(percent, length):
    start_color = colors.OKBLUE
    end_color = colors.ENDC
    if percent > 70:
        start_color = colors.WARNING
    bar = '{}'.format(start_color)
    added_end_color = False
    for i in range(length):
        if (i / length) * 100 > percent and added_end_color == False:
            bar += end_color
            added_end_color = True
        bar += '='
    return '[{}]'.format(bar)


def bytes_to_gigs(byte_count):
    return byte_count / 1.07e9


def clear_space(func):
    def wrapper():
        print()
        func()
        print()
    return wrapper


# ==================================== #
# System Information Display Functions #
# ==================================== #

@clear_space
def display_memory_usage():
    mem = psutil.virtual_memory()
    total = bytes_to_gigs(mem.total)
    percent = mem.percent
    used = bytes_to_gigs(mem.used)
    free = bytes_to_gigs(mem.free)
    buff = bytes_to_gigs(mem.buffers)
    cache = bytes_to_gigs(mem.cached)

    print("Memory Usage Information")
    print("Total\tUsed\tFree\tUse%\tBuffer\tCache")
    print("{:.2f}G\t{:.2f}G\t{:.2f}G\t{}%\t{:.2f}G\t{:.2f}G".format(
        total, used, free, percent, buff, cache))
    print(pretty_bar(percent, 50))


@clear_space
def display_cpu_usage():
    temps = psutil.sensors_temperatures()
    print("Processor Information:")
    print("  Device\tTemp")
    for temp in temps['coretemp']:
        if 'Core' not in temp.label:
            continue
        core_temp = ''
        if temp.current > temp.high / 2:
            core_temp += colors.WARNING
        else:
            core_temp += colors.OKGREEN
        core_temp += '{}'.format(round(temp.current)) + '°C' + colors.ENDC
        print('  {}\t{}'.format(temp.label, core_temp))


@clear_space
def display_disk_usage():
    usage = psutil.disk_usage('/')
    percent = usage.total / usage.used
    partitions = psutil.disk_partitions()
    print("Filesystem\tSize\tUsed\tUse%\tMount")
    for partition in partitions:
        dev = partition.device
        info = psutil.disk_usage(partition.mountpoint)
        usage = info.percent
        size = bytes_to_gigs(info.total)
        used = bytes_to_gigs(info.used)
        mount = partition.mountpoint
        print("{}\t{:.1f}G\t{:.1f}G\t{}%\t{}".format(dev, size, used, usage, mount))
        print(pretty_bar(usage, 50))


@clear_space
def display_network_information():
    addrs = psutil.net_if_addrs()
    stats = psutil.net_io_counters(pernic=True)
    print("Network Interface Information:")
    print("Interface\tAddress\t\tData In\t\tData Out")
    for interface in addrs:
        address = addrs[interface][0].address
        if ':' in address:
            continue
        data_in = bytes_to_gigs(stats[interface].bytes_recv)
        data_out = bytes_to_gigs(stats[interface].bytes_sent)
        print("{}\t\t{}\t{:.2f}G\t\t{:.2f}G".format(
            interface, address, data_in, data_out))



@clear_space
def display_proccess_information():
    pass


@clear_space
def display_battery_information():
    pass


def display_banner():
    print("""
    ____            ____                                 __ 
   / __ \___  _____/ __/___  _________ ___  ____ _____  / /_
  / /_/ / _ \/ ___/ /_/ __ \/ ___/ __ `__ \/ __ `/ __ \/ __/
 / ____/  __/ /  / __/ /_/ / /  / / / / / / /_/ / / / / /_  
/_/    \___/_/  /_/  \____/_/  /_/ /_/ /_/\__,_/_/ /_/\__/  
            """)


def start():
    display_banner()
    display_cpu_usage()
    display_network_information()
    display_memory_usage()
    display_disk_usage()


if __name__ == '__main__':
    start()

