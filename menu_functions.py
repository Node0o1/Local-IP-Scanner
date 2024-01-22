from global_imports import *
import externals
import menu_functions

def main():
    proxy_list=list()
    prxout = list()
    try: menu_functions.banner()
    except: print(f'{RED}Please make you sure have an internet connection and python is added to path and then pip install requirements.txt.{YELLOW}')
    else:
        scan_type = menu_functions.menu_selection()
        match scan_type:
            #http scan
            case '1':
                try: proxy_list = externals.import_file()
                except: print('Please check spelling and file path.')
                else:
                    check_connectivity_func = externals.check_device_connectivity
                    print(f'{GREEN}Scanning http ip/domains for connectivity.{chr(0x0a)}Please wait...{YELLOW}')  
            #live local devices
            case '2':
                try: proxy_list = externals.get_local_live_ips()
                except: print(f'{RED}IP info not found. Please be sure you are connected to a network.{YELLOW}')
                else:
                    check_connectivity_func = externals.check_device_connectivity
                    print(f'\n{GREEN}Scanning local addresses ( {CYAN}{proxy_list[0]}{GREEN} - {CYAN}{proxy_list[-1]}{GREEN} ).{chr(0x0a)}Please wait...{YELLOW}')    
            #live device host names
            case '3':
                try: proxy_list = externals.import_file()
                except: print('Please check spelling and file path.')
                else:
                    check_connectivity_func = externals.local_ip_to_hostname
                    print(f'\n{GREEN}Scanning live local IPs for host name.{chr(0x0a)}Please wait...{YELLOW}')  
            case '4':
                print(f'{GREEN}Goodbye.{RESET}')  
                exit()
            #exit
            case _:
                print(f'{RED}Selection error. Goodbye.{RESET}')
                exit()

        try: prxout = externals.process(proxy_list, check_connectivity_func)
        except: None
        else:
            externals.print_prx(prxout)
            user = str(input(f'\n{YELLOW}Do you want to write the output to a file.txt? (Y/N): {MAGENTA}'))
            if(user.upper()=='Y'):
                externals.write_prx(prxout)

    finally: input(f'\n{YELLOW}Exiting Scanner\nPress {RED}[{CYAN}ENTER{RED}]{YELLOW} to exit: {RESET}')

if __name__=='__main__':
    main()