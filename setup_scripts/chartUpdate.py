import shutil 
import sys


def checkversionArgument():
    if sys.argv[1]:
        return sys.argv[1]
    else:
        print("Missing Release version")
        sys.exit(98) 
def takeBackup():

    try:        

       shutil.copy('geoapp/Chart.yaml', 'geoapp/chart_bk.yaml')
    except Exception as e:
        print(f"Error: {e}")   

def chartModif(chart_version):
    try: 
      with open("geoapp/Chart.yaml", 'r') as f:
         content = f.readlines()
    except Exception as e:
        print(f"Error: {e}") 
        sys.exit(99)
    else:       
        
       with open("geoapp/Chart.yaml" , 'w')  as f1:
        for line in content:
            if 'version:' in line:
                f1.write(f'version: {chart_version}\n')
            elif 'appVersion:' in line: 
                f1.write(f'appversion: {chart_version}\n') 
            else:
                f1.write(line)
        print(f"Chart updated to version {chart_version}")  
def main():
    App_VERSION=checkversionArgument()
    takeBackup()
    chartModif(App_VERSION)

if __name__== "__main__":
    main                  
     
   
           