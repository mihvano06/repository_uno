#####1
from Bio import Entrez, SeqIO
Entrez.email = "mihvanya@gmail.com"
species_names = ["Brassica oleracea", "Solanum lycopersicum"]
records = []
for species in species_names:
    search_handle = Entrez.esearch(db="nucleotide", term=f"{species} complete cds", retmax=5)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    id_list = search_results["IdList"]
    for seq_id in id_list:
        fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="gb", retmode="text")
        records.append(SeqIO.read(fetch_handle, "genbank"))
        fetch_handle.close()
output_file = "merged_sequences.gb"
with open(output_file, "w") as output_handle:
    SeqIO.write(records, output_handle, "genbank")
print(f"Все записи успешно сохранены в {output_file}.")

#####2
from Bio import  SeqIO
input_file = 'merged_sequences.gb'
records = []
for record in SeqIO.parse(input_file, 'genbank'):
    gc_content = (record.seq.count('G') + record.seq.count('C')) / len(record.seq)
    records.append((record.id, str(record.description), gc_content))
records.sort(key=lambda x: x[2])
for record in records:
    print(f"{record[0]}: {record[1]} gene, complete cds, GC = {record[2]:.16f}")

#####3
from Bio import SeqIO
genbank_file = "merged_sequences.gb"
for record in SeqIO.parse(genbank_file, "genbank"):
    print(f"Обработка записи: {record.id}")
    for feature in record.features:
        if feature.type == "mRNA":
            protein_sequences = []
            for location in feature.location:
                if location.type == "CDS":
                    seq = record.seq[location.start:location.end]
                    protein = seq.translate()
                    protein_sequences.append(str(protein))
                    print(f"Белковая последовательность: {protein}")
