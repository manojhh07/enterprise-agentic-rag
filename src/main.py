from loaders.pdf_loader import load_pdf

def main():

    documents = load_pdf("data/employee_handbook.pdf")

    print("="*50)

    print(f"Total Pages Loaded : {len(documents)}")

    print("="*50)

    print("\n First Document \n")

    print(documents[0])

    print("\n Pagfe Content \n")

    print(documents[0].page_content)

    print("\n metadata \n")

    print(documents[0].metadata)

if __name__ == "__main__":
    main()