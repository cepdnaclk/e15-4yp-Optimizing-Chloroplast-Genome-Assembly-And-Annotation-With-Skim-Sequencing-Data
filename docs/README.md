---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e15-4yp-Optimizing-chloroplast-genome-assembly-and-annotation-with-skim-sequencing-data
title: Optimizing chloroplast genome assembly and annotation with skim sequencing data
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Optimizing chloroplast genome assembly and annotation with skim sequencing data

#### Team

- E/15/209, H. Kithma Madhushani, [email](mailto:kithmamadushani1@gmail.com)
- E/15/233, Nipuni Muthucumarana, [email](mailto:nipunimuthucumarana@gmail.com)
- E/15/325, Chalani Weerarathna, [email](mailto:chalanisweerarathna@gmail.com)

#### Supervisors

- Dr. Asitha Bandaranayake, [email](mailto:asithab@eng.pdn.ac.lk)
- Prof. Pradeepa Bandaranayake, [email](mailto:pcgunathilake@gmail.com)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Links](#links)

---

## Abstract

Chloroplast genes and genomes play an important role in plant phylogeny and speciesidentification. Skim sequencing is getting low coverage genome sequencing data that has,nuclear, choloroplast and mitochondria genome sequences. Since the fast developmentof high throughput sequencing technologies, it’s low cost to urge the low coverage dataof the whole genome (usually concerning 20-30GB data), that is enough to assemblea whole chloroplast genome. To date, there are several assembly processes/pipelinesdesigned to assemble a whole chloroplast genome. However, what proportion knowledgeis required or really utilized in such analysis is a problem. Having such information canfacilitate biologists to style their experiments properly and cost-effectively. Biologistsexpect a straightforward, quick and easy procedure to assemble and annotate a circularchloroplast genome from Illumina NGS data.In this project, we’ll analysis the present procedures for chloroplast genome assemblyand annotation, and work on developing the strategies to spot and choose the best set(s)of data and the procedure(s) to assemble a given chloroplast genome as accurately andefficiently, by statistical, computational and heuristical strategies.

## Related works

The process of chloroplast genomes assembly has different strategies. Consider WholeGenome Sequencing (WGS) data and there are two main steps required for the process.First one is the extraction of chloroplast reads from the sequencing data and the secondstep is resolution and assembly of the special circular structure including the IRs. Thefirst step can be achieved by mapping the reads to a chloroplast reference. To do thisprocess, assemblers can use k-mers. that are highly repeated in the chloroplast reads.Another method is to use the highly represented reads from the data set without usingreference-based approach. Apart from those two methods. There is another methodcalled NOVOPlasty, which combines the above two approaches by using a chloroplastreference as seed and then trying a simultaneous assemble of reads based on list of k-mers.

Genome assembly process is called as a sequence assembly. There are two ways to do asequence assembly.
1. De Novo assembly
2. Reference mapping assembly

'De Novo' means start from the beginning. As the name of it, ’De Novo’ assemblersare the type of program that assembling a large of short DNA sequence and create fullsequences of the original chromosomes from which the DNA originated without the useof a reference genome. As an example in ’De novo assemblers’ does not use any priorknowledge of the source DNA sequence length, layout, or composition.There are two common types of ’De Novo assemblers’ named as ’greedy algorithmassemblers’ which aim for local optima in alignments of smaller reads and ’graph methodassemblers’ which aim for global optima. String graph and De Bruijn graph [6] are twocommon graph methods. There is a common protocol for the De Novo assembly.

There are several bioinformatic tools available for the De Novo genome assemblyprotocol [7]. Those tools can be used in three areas.
1. Tools for reading and quality control
- FastQC
-  NGS QC
- Trimmomatic
2. Tools for assembly
- NOVOPlasty
- Velvet Optimizer
- Faster Statics
- Spades
- Soap-denovo
3. Tools for determining the suitability of a draft set of contigs
- QUAST
- Manuve assembly metric
- CLC BioWorkbench

On the other hand ‘reference mapping assemblers’ are a type of program that assem-bling reads against and existing backbone sequence. It builds a sequence that is similarbut not necessarily identical to the backbone sequence. In this assembly method, partswith multiple or no matches are usually left for another assembling technique to lookinto.Instead of using De Novo assembler and ‘Reference mapping assembler’ separately,the combination of these two methods provides an effective and powerful tool to improvegenome assembly by integrating information of a related genome. This method is calledReference-guided de novo assembly approach.

Main Assembly Softwares
1.GetOrganelle
2.Fast-plast
3.NovoPlasty

Some factors were taken into consideration when testing the tools and those factors areassembly time, memory and CPU utilization. Time requirement for the assembly is agood measure as it shows huge differences from tool to tool. Variation in run time differsfrom few minutes to several hours. Input data and number of threads used also affectedfor the time requirement. In the experiment, tools are tested with a time limit of 48h.Some assemblies exceeded that time limit. According to the test results, IOGA andFast-Plast. followed by ORG.Asm and GetOrganelle took the longest time periodfor the assembly generation. ChloroExtractor can be considered as the most timeefficient tool and it was somewhat faster than NOVOPlasty and Chloroplast assemblyprotocol.Having access to multithreading is beneficial for the tools. Chloroplast assemblyprotocol, chloroExtractor, GetOrganelle and Fast-Plast methods profited from havingmultiple threads. But NOVOPlasty and ORG-Asm cannot be recognized independentlyby using multithreading because both of them required almost the same time to utilize 1,2, 4 or 8 threads.When considering the memory and CPU usage, for the same input data set and forthe same number of threads, disk usage and peak memory were recorded and also, meanand peak values of CPU usage recorded for each an every assembler. Although memoryusage patterns shown by ChloroExtractor and IOGA assemblers influenced a little bythe size of the input data, other assemblers’ peak memory usage influenced up to aconsiderable level. If the input date size is higher related to their memory and CPUusage, assemblers are profited from having higher number of threads. But disk usage ofall assemblers does not depend on either size of the input data or the number of threads.

## Methodology

The main goal of this research is to find the most optimal chloroplast assembly tool toassemble whole genome sequencing data. As an example, we are going to assemble acinnamon data set using the best three tools which we identified from the research andthen the results from each tool will be compared. From the comparison we can identifythe weak points and strengths of each tool. Then we build a new pipeline includingall identified strengths, by combining different methods together. Using the new tool,we can assemble the same cinnamon data set and check whether the results are moreaccurate than the results obtained previously from each tool. We can repeat the sameprocess for different newly built pipelines with different strengths.

## Experiment Setup and Implementation

We tested for several assembly tools for their run time, cpu usage and memory usage with different datasets considering their accuracy. Based on thee results  given we develop a workflow for Optimizing chloroplast genome assembly and annotation with skim sequencing data.

## Results and Analysis

We have attach our results and comparison in the root folder of the repository.

## Conclusion

About nearly half of the analyzed WGS data without available chloroplast genome,complete assemblies can be generated using the assembly tools.There are many tools for genome assembly by the present. GetOrganelle , Fast-Plast , NOVOPlasty , ORG.Asm , IOGA and chloroExtractor are someof them. Scientsts tend to compare overall performance of the different chloroplastassemblers depending on the various assessment criteria.When we compared the general performance of the different chloroplast assemblingtools, we need to consider various criteria. The most straightforward assembler in general,both on recreated and genuine information, was accomplished by GetOrganelle. Fast-Plast performed almost likewise on most information. These two devices supplementeach other, together with the instrument can do successful assemblies of full chloroplastsin situations where the contrary instrument comes up short. GetOrgane is the onlytool that can generate assemblies for 15 different datasets . Fast-Plast can generateassemblies for only 3 datasets that vanquished every single other tool. NOVOPlasty was the sole another device that would produce a get together that wasn’t created withthe other constructing assembly tool. Fast- Plast, NOVOPlasty, and ORG.Asm delivered the most valuable outcomes, and along these lines, rerunning the device after afailed endeavor could be an authentic methodology. ChloroExtractor  has producedvery few chloroplast assemblies, but requires few materials and is straightforward toinstall and use. Both IOGA and Chloroplast protocol protocols had unsatisfactoryperformance and did not return to reliable chloroplast conventions. These tools canreconstruct the chloroplast genome even without available reference genomes.

Therefore, among the above-mentioned tools, GetOrganelle can be used as adefault option for chloroplast assemblies. Fast-Plast is the second option and the thirdoption can be NOVOPlasty.But all tools do not succeed in generating complete chloroplast assemblies andtherefore, we have to determine the strengths and weaknesses of the specific tools.Sometimes it may be necessary to combine different methods or manually explore theparameter space for generating complete chloroplast assemblies. But most of the time,reconstructing thousands of chloroplast genomes is feasible using the currently availabletools.When considering the annotation tools, most of the time, Dogma has been widelyused for gene prediction in chloroplasts. Until recently, it was the only tool specific tochloroplast genomes, that explains its success for the annotation of genomes. Now moreconsistent annotation of genes is produced with GeSeq when compared to the Dogmasuggesting that annotation of most of the previously annotated chloroplast genomesshould now be updated.


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/repository-name)
- [Project Page](https://cepdnaclk.github.io/repository-name)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
