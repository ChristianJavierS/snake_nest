import argparse
import os
import logging

class PenTestingTree:
    def __init__(self, company_name):
        self.company_name = company_name
        self.base_folder = os.path.join(os.getcwd(), company_name)
        self.subfolders = ["EPT", "IPT"]
        self.sub_subfolders = ["evidence", "logs", "scans", "scope", "tools"]
        self.evidence_subfolders = ["credentials", "data", "screenshots"]

    def create_folders(self):
        try:
            if not os.path.exists(self.base_folder):
                os.mkdir(self.base_folder)
                logging.info(f"Created folder: {self.base_folder}")

            for subfolder in self.subfolders:
                subfolder_path = os.path.join(self.base_folder, subfolder)
                if not os.path.exists(subfolder_path):
                    os.mkdir(subfolder_path)
                    logging.info(f"Created folder: {subfolder_path}")

            ept_folder = os.path.join(self.base_folder, "EPT")
            for subfolder in self.sub_subfolders:
                subfolder_path = os.path.join(ept_folder, subfolder)
                if not os.path.exists(subfolder_path):
                    os.mkdir(subfolder_path)
                    logging.info(f"Created folder: {subfolder_path}")

            ipt_folder = os.path.join(self.base_folder, "IPT")
            for subfolder in self.sub_subfolders:
                subfolder_path = os.path.join(ipt_folder, subfolder)
                if not os.path.exists(subfolder_path):
                    os.mkdir(subfolder_path)
                    logging.info(f"Created folder: {subfolder_path}")

            for folder in (ept_folder, ipt_folder):
                evidence_folder = os.path.join(folder, "evidence")
                for subfolder in self.evidence_subfolders:
                    subfolder_path = os.path.join(evidence_folder, subfolder)
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                        logging.info(f"Created folder: {subfolder_path}")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Create a pentesting tree folder structure.")
    parser.add_argument("-n", "--name", required=True, help="Company or machine target name")
    args = parser.parse_args()
   
    logging.basicConfig(filename='pentesting_tree.log', level=logging.INFO)  # Add logging configuration

    pentesting_tree = PenTestingTree(args.name)
    pentesting_tree.create_folders()

if __name__ == "__main__":
    main()
