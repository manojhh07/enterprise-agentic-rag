from loaders.pdf_loader import load_pdf
from chunking.text_splitter import split_documents


def main():

    documents = load_pdf("data/employee_handbook.pdf")

    print("=" * 60)
    print(f"Total Documents : {len(documents)}")
    print("=" * 60)

    chunks = split_documents(documents)
    print(f"Total Chunks {len(chunks)}") 

    print("\n First Chunk \n")

    print(chunks[0].page_content)

    print("\n Metadata \n")

    print(chunks[0].metadata)   

    print("=" * 60)
    for i in range(3):

        print("=" * 60)

        print(f"Chunk {i+1}")

        print(chunks[i].page_content)

        print("\nMetadata")

        print(chunks[i].metadata)

        print()
    


if __name__ == "__main__":
    main()