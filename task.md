# Task
Here is the text extracted from the HTML document:

**POLAR @ SemEval-2026**
Links: Discord | Google Group | GitHub

# Subtasks

Our task consists of three subtasks. Participants may choose to compete in one or more of the three subtasks. Each subtask is designed to address a specific aspect of polarization detection and analysis in multilingual social media content.

## Dataset Information
Data sources include news websites, Reddit, blogs, Bluesky, and regional forums, covering events such as elections, conflicts, gender rights, migration, and more. Each language contains 3,000–5,000 annotated instances.

A few sample instances are provided here for review, and additional trial data can be found at: **TRIAL DATA**

***

## Languages Covered
The task covers **22 languages** across different cultural and geographical contexts:

Amharic, Arabic, Bengali, Burmese, Chinese, English, German, Hausa, Hindi, Italian, Khmer, Nepali, Odia, Persian, Polish, Punjabi, Russian, Spanish, Swahili, Telugu, Turkish, Urdu.

***

## Subtask 1: Polarization Detection
If a text includes one or more of the polarized specified characteristics, it is classified as polarized. Conversely, social media texts that do not display any of these characteristics are classified as non-polarized.
Therefore, a given text is classified into one of two categories:
1. Text that contains/shows polarized opinion (Yes)
2. Text that does not contain polarized opinion (No)

Note: Only texts that clearly reflect attitude polarization are classified as such, with consideration of the context and the overall meaning of the text, not just individual words or phrases.

**Subtask-1: Binary classification:** to determine whether a post contains polarized content (Polarized or Not Polarized).

| id | text | polarization |
| :--- | :--- | :--- |
| 2745 | Find yourself a west bank settler gf | 1 |
| 2738 | Fascist oligarchs now control the USA | 1 |
| 3184 | Someone end this lunatic before he starts ethnic cleansing | 1 |
| 1614 | The EU is increasing military aid to Ukraine to one billion euros the press release on the website of the Council of Europe. | 0 |
| 716 | House drafts bill to strike Iran proxies amid IsraelHamas | 0 |
| 309 | Contested races across county early voting | 0 |

[Link: Go to Subtask-1 Competition]

***

## Subtask 2: Polarization Type Classification
Looking at the given social media texts, the type or target polarization is classified as follows:
1. **Political/ideological polarization:** This type of extremism focuses on division, intolerance, and conflict between political parties and followers. Political polarization refers to political beliefs and affiliations becoming more extreme. People may identify more strongly with their political party, leading to deeper divides and a reduced willingness to compromise. It broadens ideological differences between political groups.
2. **Racial or ethnic polarization:** This type of polarization focuses on ethnic identity or racial origin and incites division, intolerance, and conflict between ethnic groups or races. This type of polarization arises when individuals identify more strongly with their own racial or ethnic group, leading to increased separation, mistrust, or conflict with individuals from other groups.
3. **Religious polarization:** This type of polarization focuses on religious identity and incites division, intolerance, and conflict between religious followers.
4. **Gender polarization:** This type of polarization refers to the exclusion, discrimination, and marginalization of individuals based on their gender. **Sexual orientation polarization:** This refers to the increasing division and distinction between different sexual orientations within society, often leading to heightened tensions, misunderstandings, conflicts, or marginalization among various groups.
5. **Other:** polarization texts targeting other groups/identities such as economy, technology, media, polarization, etc.

**Subtask-2: Multi-label classification:** to identify the target of polarization as one of the following categories: Political, Racial/Ethnic, Religious, Gender/Sexual or Other.

| id | text | political | racial/ethnic | religious | gender/sexual | other |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2745 | Find yourself a west bank settler gf | 1 | 0 | 0 | 1 | 0 |
| 2738 | Fascist oligarchs now control the USA | 1 | 0 | 0 | 0 | 0 |
| 3184 | Someone end this lunatic before he starts ethnic cleansing | 1 | 1 | 0 | 0 | 0 |

[Link: Go to Subtask-2 Competition]

***

## Subtask 3: Manifestation Identification
A message/ text on social media is considered to be polarizing if it exhibits one or more of the following characteristics:
1. **Stereotype:** This manifestation occurs when a message generalizes certain characteristics of individuals to all members of a group, ignoring individual differences. Stereotypes simplify complex personalities into one-size-fits-all representations.
2. **Vilification:** Vilification appears when a text defames or demonizes a particular group, person, or entity, often inciting fear through exaggeration, misrepresentation, or biased framing that portrays the subject in a harmful or negative light.
3. **Dehumanization:** This occurs when language strips a group or individual of human qualities or dignity, often by comparing them to animals, machines, or objects, or by otherwise denying their humanity and individuality.
4. **Extreme Language and Absolutism:** This manifestation involves the use of extreme or absolutist language that reflects polarized attitudes, such as words like “always,” “never,” “worst,” or “best.” It often presents issues in dichotomous terms such as “us vs. them” or “right vs. wrong.”
5. **Lack of Empathy or Understanding:** This occurs when the text shows no empathy or understanding for others’ perspectives or experiences. It may involve marginalizing alternative viewpoints or refusing to understand or relate to them.
6. **Invalidation:** Invalidation appears when a text denies or rejects the identity or existence of certain people or groups, dismissing their legitimacy or right to exist.

**Subtask-3: Multi-label classification:** to classify how polarization is expressed, with multiple possible labels including Stereotype, Vilification, Dehumanization, Extreme Language, Lack of Empathy", or Invalidation.

**NOTE: Italian and Russian languages are not included in this subtask.**

| id | text | stereotype | vilification | dehumanization | extreme_language | lack_of_empathy | invalidation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2745 | Find yourself a west bank settler gf | 1 | 1 | 0 | 0 | 0 | 0 |
| 2738 | Fascist oligarchs now control the USA | 0 | 1 | 0 | 1 | 0 | 0 |
| 3184 | Someone end this lunatic before he starts ethnic cleansing | 1 | 1 | 0 | 1 | 0 | 0 |


```
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc, shadows}

\begin{document}

\begin{tikzpicture}[
    % Define styles for the boxes
    base/.style={
        draw, 
        thick, 
        align=center, 
        minimum height=1cm, 
        font=\sffamily\bfseries
    },
    input/.style={
        base, 
        fill=blue!10, 
        draw=blue!40!black, 
        rounded corners=5pt, 
        minimum width=6cm
    },
    encoder/.style={
        base, 
        fill=green!10, 
        draw=green!40!black, 
        rounded corners=10pt, 
        minimum width=8cm, 
        minimum height=2cm,
        drop shadow
    },
    task/.style={
        base, 
        fill=orange!10, 
        draw=orange!40!black, 
        rounded corners=5pt, 
        minimum width=3.5cm,
        font=\sffamily\small\bfseries
    },
    output/.style={
        base, 
        fill=gray!10, 
        draw=gray!50!black, 
        dashed,
        rounded corners=5pt, 
        minimum width=3.5cm
    },
    gate/.style={
        circle, 
        draw, 
        thick, 
        fill=white, 
        minimum size=0.8cm,
        inner sep=0pt,
        font=\Large\bfseries
    },
    % Define arrow styles
    arrow/.style={
        -{Latex[length=3mm, width=2mm]}, 
        thick, 
        draw=black!80
    },
    line/.style={
        thick, 
        draw=black!80
    }
]

    % --- Nodes ---

    % 1. Input Layer
    \node (input) [input] {Input};

    % 2. Shared Encoder
    \node (encoder) [encoder, above=0.8cm of input] {\Large Shared Encoder\\ \small (BERT-like)};

    % 3. Task Heads
    % Center Head (Subtask 2) - We position this first as the anchor
    \node (st2) [task, above=1.5cm of encoder] {Subtask 2 (Head)\\Polarization Type};
    
    % Left Head (Subtask 1)
    \node (st1) [task, left=0.5cm of st2] {Subtask 1 (Head)\\Polarization Detection};
    
    % Right Head (Subtask 3)
    \node (st3) [task, right=0.5cm of st2] {Subtask 3 (Head)\\Manifestation ID};

    % 4. Gating Operations (Multiplying Gates)
    % Placed above Subtasks 2 and 3
    \node (mult2) [gate, above=1cm of st2] {$\times$};
    \node (mult3) [gate, above=1cm of st3] {$\times$};

    % 5. Final Outputs
    \node (out1) [output, above=2.3cm of st1] {Final Output 1\\(Polarized Y/N)};
    \node (out2) [output, above=0.5cm of mult2] {Final Output 2\\(Type)};
    \node (out3) [output, above=0.5cm of mult3] {Final Output 3\\(Manifestation)};

    % --- Connections ---

    % Input -> Encoder
    \draw[arrow] (input) -- (encoder);

    % Encoder -> Task Heads
    \draw[arrow] (encoder.north -| st1.south) -- (st1.south);
    \draw[arrow] (encoder.north -| st2.south) -- (st2.south);
    \draw[arrow] (encoder.north -| st3.south) -- (st3.south);

    % Subtask 1 Flow (Direct to Output)
    \draw[arrow] (st1.north) -- (out1.south);
    
    % --- The Gating Logic (Fixed) ---
    % 1. Define a coordinate "split" that is vertically aligned with the Gates (mult2)
    %    and horizontally aligned with Subtask 1 (st1).
    \path (st1.north |- mult2) coordinate (split);

    % 2. Draw line UP from Subtask 1 to the split height
    \draw[line] (st1.north) -- (split);

    % 3. Draw horizontal line ACROSS to the gates
    %    We draw to the 'west' (left side) of the multiplier circles.
    \draw[arrow] (split) -- (mult2.west) node[midway, above, font=\small\sffamily] {Mask ($0$ or $1$)};
    \draw[arrow] (mult2.east) -- (mult3.west);

    % Decorative dot at the branch point
    \filldraw (split) circle (2pt); 

    % Subtask 2 Flow (Up -> Multiply -> Out)
    \draw[arrow] (st2.north) -- (mult2.south);
    \draw[arrow] (mult2.north) -- (out2.south);

    % Subtask 3 Flow (Up -> Multiply -> Out)
    \draw[arrow] (st3.north) -- (mult3.south);
    \draw[arrow] (mult3.north) -- (out3.south);

    % --- Annotations ---
    \node [right=0.2cm of mult3, text width=3.2cm, font=\sffamily\footnotesize, align=left] 
        {\textbf{Inference Gating:}\\If Subtask 1 predicts "0", the mask zeros out predictions for Subtasks 2 \& 3.};

\end{tikzpicture}

\end{document}
```