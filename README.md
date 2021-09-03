# RNA-seq Quality Assessment Assignment - Bi 623 (Summer 2021)

Be sure to upload all relevant materials by the deadline and **double check** to be sure that your off-line repository is up-to-date with your on-line repository. Answers to the questions can be submitted as Github markdown or ```pdf```.

## Objectives
The objectives of this assignment are to use existing tools for quality assessment and adaptor trimming, compare the quality assessments to those from your own software, and to demonstrate your ability to summarize other important information about this RNA-Seq data set.

### Data: 
Each of you will be working with 2 of the demultiplexed file pairs. For all steps below, process the two libraries separately. Library assignments are here: ```/projects/bgmp/shared/Bi623/QAA_data_assignments.txt```

My particular files are: ```29_4E_fox_S21_L008	8_2F_fox_S7_L008```

The demultiplexed, gzipped .fastq files are here: ```/projects/bgmp/shared/2017_sequencing/demultiplexed/```

## Do not move, copy, or unzip these data!

# Part 1 – Read quality score distributions

1. Using ```FastQC``` via the command line on Talapas, produce plots of quality score distributions for R1 and R2 reads. Also, produce plots of the per-base N content, and comment on whether or not they are consistent with the quality score plots.

29_4E_fox_S21_L008 R1

<img width="682" alt="Screen Shot 2021-09-01 at 15 30 43" src="https://user-images.githubusercontent.com/71104613/131753818-3cb1acf6-c305-4df6-999f-68b7da818fee.png">
<img width="671" alt="Screen Shot 2021-09-01 at 15 31 45" src="https://user-images.githubusercontent.com/71104613/131753896-8b22b921-588a-45ae-9091-f64142270085.png">
29_4E_fox_S21_L008 R2

<img width="678" alt="Screen Shot 2021-09-01 at 15 32 13" src="https://user-images.githubusercontent.com/71104613/131753952-97ff403a-1d51-4b8e-8bc0-6846ca4a2b3c.png">
<img width="675" alt="Screen Shot 2021-09-01 at 15 32 33" src="https://user-images.githubusercontent.com/71104613/131753985-a7246531-8128-4d6c-a427-0830fdcb355c.png">
8_2F_fox_S7_L008 R1

<img width="683" alt="Screen Shot 2021-09-01 at 15 33 01" src="https://user-images.githubusercontent.com/71104613/131754030-8803e48b-6366-4242-badd-773c919cedd3.png">
<img width="678" alt="Screen Shot 2021-09-01 at 15 33 17" src="https://user-images.githubusercontent.com/71104613/131754048-3c717562-fd66-4d8f-b583-4d43d7cac734.png">
8_2F_fox_S7_L008 R2

<img width="694" alt="Screen Shot 2021-09-01 at 15 33 44" src="https://user-images.githubusercontent.com/71104613/131754091-7909be76-f163-4923-a2d8-c7be5abebc88.png">
<img width="689" alt="Screen Shot 2021-09-01 at 15 34 02" src="https://user-images.githubusercontent.com/71104613/131754134-ef1535f0-2614-4d8b-8b93-157affc14b00.png">

2. Run your quality score plotting script from your Demultiplexing assignment from Bi622. Describe how the ```FastQC``` quality score distribution plots compare to your own. If different, propose an explanation. Also, does the runtime differ? If so, why? 

```
The amount of time it took to run my plotting script was considerably slower than the fastqc plot generation. It takes a while to do the same thing in Python, while Java might just be comparably faster, since that's what fastqc is programmed in.
``` 


29_4E_fox_S21_L008 R1

![29_R1_out](https://user-images.githubusercontent.com/71104613/131964714-0d931736-7346-46b7-84e6-4b880c38a681.png)

29_4E_fox_S21_L008 R2

![29_R2_out](https://user-images.githubusercontent.com/71104613/131964723-f8caadc5-cd18-4a67-90f5-21e8c6f95679.png)

8_2F_fox_S7_L008 R1

![8_R1_out](https://user-images.githubusercontent.com/71104613/131964676-fc19d61f-5d3e-48cb-82c5-76657029fea0.png)

8_2F_fox_S7_L008 R2

![8_R2_out](https://user-images.githubusercontent.com/71104613/131964687-2ef6904b-c35c-4949-8bb7-aa0b9f488a32.png)


3. Comment on the overall data quality of your two libraries.

```
both libraries are honestly very good in my opinion. Qscores are higher than I've seen as of now. 
```

# Part 2 – Adaptor trimming comparison

4. Create a new conda environment called ```QAA``` and install ```cutadapt``` and ```Trimmomatic```. Google around if you need a refresher on how to create conda environments. Make sure you check your installations with:
    - ```cutadapt --version``` (should be 3.4)
    -  ```trimmomatic -version``` (should be 0.39)

5. Using ```cutadapt```, properly trim adapter sequences from your assigned files. Be sure to read how to use ```cutadapt```. Use default settings. What proportion of reads (both forward and reverse) were trimmed?



    <details>
    <summary>Try to determine what the adapters are on your own. If you cannot (or if you do, and want to confirm), click here to see the actual adapter sequences used.</summary>
  
    R1: ```AGATCGGAAGAGCACACGTCTGAACTCCAGTCA```
    
    R2: ```AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT```
    </details>

    - *Sanity check*: Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. Report the commands you used, the reasoning behind them, and how you confirmed the adapter sequences.

6. Use ```Trimmomatic``` to quality trim your reads. Specify the following, in this order:
    - LEADING: quality of 3
    - TRAILING: quality of 3
    - SLIDING WINDOW: window size of 5 and required quality of 15
    - MINLENGTH: 35 bases

    Be sure to output compressed files and clear out any intermediate files.

7. Plot the trimmed read length distributions for both R1 and R2 reads (on the same plot). You can produce 2 different plots for your 2 different RNA-seq samples. There are a number of ways you could possibly do this. One useful thing your plot should show, for example, is whether R1s are trimmed more extensively than R2s, or vice versa. Comment on whether you expect R1s and R2s to be adapter-trimmed at different rates. 

# Part 3 – Alignment and strand-specificity
8. Install sofware. In your QAA environment, use conda to install:
    - star
    - numpy
    - pysam
    - matplotlib

    Then ```pip install HTSeq```

8. Find publicly available mouse genome fasta files (Ensemble release 104) and generate an alignment database from them. Align the reads to your mouse genomic database using a splice-aware aligner. Use the settings specified in PS8 from Bi621.

    *Hint* - you will need to use gene models to perform splice-aware alignment, see PS8 from Bi621.
    
9. Using your script from PS8 in Bi621, report the number of mapped and unmapped reads from each of your 2 sam files. Make sure that your script is looking at the bitwise flag to determine if reads are primary or secondary mapping (update your script if necessary).

10. Count reads that map to features using htseq-count. You should run htseq-count twice: once with ```--stranded=yes``` and again with ```--stranded=no```. Use default parameters otherwise.

```

htseq-count --stranded=yes Mus_musculus.GRCm39.dna.primary_assembly.ens104.STAR_2.7.9a1Aligned.out.sam ./mouse_fasta/Mus_musculus.GRCm39.104.gtf > HTS_S_yes_8_2F.tsv 

__no_feature	30658192
__ambiguous	26184
__too_low_aQual	61684
__not_aligned	1222586
__alignment_not_unique	1588617


htseq-count --stranded=no Mus_musculus.GRCm39.dna.primary_assembly.ens104.STAR_2.7.9a1Aligned.out.sam ./mouse_fasta/Mus_musculus.GRCm39.104.gtf > HTS_S_no_8_2F.tsv

__no_feature	3148692
__ambiguous	1555558
__too_low_aQual	61684
__not_aligned	1222586
__alignment_not_unique	1588617


htseq-count --stranded=yes Mus_musculus.GRCm39.dna.primary_assembly.ens104.STAR_2.7.9aAligned.out.sam ./mouse_fasta/Mus_musculus.GRCm39.104.gtf > HTS_S_yes_29_4E.tsv

__no_feature	1811726
__ambiguous	1334   *****
__too_low_aQual	3642
__not_aligned	56506
__alignment_not_unique	87551

htseq-count --stranded=no Mus_musculus.GRCm39.dna.primary_assembly.ens104.STAR_2.7.9aAligned.out.sam ./mouse_fasta/Mus_musculus.GRCm39.104.gtf  > HTS_S_no_29_4E.tsv

__no_feature	119362
__ambiguous	98624   *****
__too_low_aQual	3642
__not_aligned	56506
__alignment_not_unique	87551
```

11. Demonstrate convincingly whether or not the data are from “strand-specific” RNA-Seq libraries. Include any comands/scripts used. Briefly describe your evidence, using quantitative statements (e.g. "I propose that these data are/are not strand-specific, because X% of the reads are y, as opposed to z.").

    *Hint* - recall ICA4 from Bi621.

**To turn in your work for this assignment**:
Upload your Talapas batch script/code, FastQC plots, mapped/unmapped read counts, counts files generated from htseq-count, answers to questions, and any additional plots/code to github. You should create at most 2 files for submission (R markdown and the rendered pdf file) containing all these elements. The three parts of the assignment should be clearly labeled. Be sure to title and write a figure legend for each image/graph/table you present.
