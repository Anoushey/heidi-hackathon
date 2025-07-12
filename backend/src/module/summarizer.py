import json
from google import genai


PROMPT = """
I'll give you a medical transcript, please response with json format that has this keys:
1. appointments
   a. who (text)
   b. why (text)
2. diagnosis (list(text))
3. precautions (list(text))
   a. precaution (text)
   b. reason (text)
4. medications (list(text))
   a. name (text)
   b. reason (text)
   c. frequency (text)
5. things_to_do (list(dict))
   a. what to do
   b. period
   b. reason
   
[DESCRIPTION]
1. appointments: where's the next appointment will be held (if available)
   a. who: with whom will the next appointment be held
   b. why: why the patient needs to have the next appointment
   c. when: what date and time is the next appointment
2. diagnosis: explain it to patient within layperson terms without the usage of medical terminology
3. precautions: what are the precautions that need to be taken by the patient.
   a. what: what is the precaution to be taken. Explain in layperson terms
   b. why: Explain why you should take this precaution in layperson terms
4. medications: what are the medications the patient need to take
   a. name: medication name
   b. reason: why is the medication to be taken
   c. frequency: how often should the medication be taken by the patient
5. things_to_do: what are the things the patient need to do (for example walking exercise in the morning)
   a. what: what's the things needed to do
   b. period: daily, weekly, monthly in this format
       b.1. daily, weekly, month
       b.2. time
   c. reason: reason for doing this
I want the language to be for a layperson patient with no prior knowledge of medicine, not a clinical / doctor

```
{content}
```
"""


class Summarizer:
    def __init__(self):
        self._client = genai.Client()
        self._model = "gemini-2.5-flash"

    def summarize(self, content: int):
        data = PROMPT.format(content=content)
        out = self._client.models.generate_content(model=self._model, contents=data)
        out = out.text.strip("```").strip("json")
        out = json.loads(out)
        return out


if __name__ == "__main__":
    obj = Summarizer()
    content = """
History:
- 39 year old male
- Reports sudden onset left-sided chest pain starting last night, becoming sharper.
- Pain has been constant for approximately 8 hours.
- Described as sharp, 7-8/10 severity.
- Worsened by lying down and deep breath.
- Alleviated by not lying down.
- Associated symptoms: lightheadedness, trouble breathing since pain started, racing heart. Denies loss of consciousness, sick feeling, fevers, chills, abdominal pain, urinary problems, bowel problems, cough, blood with cough, wheeze, night sweats, rashes. Reports neck swelling.
- Denies prior similar episodes.
- Reports moving furniture when pain started, but denies injury.

Past Medical History:
- Denies prior medical conditions, recent hospitalisations, prior surgeries.
- Denies medication allergies.
- Medications: nil
- Immunisations: up to date.
- Social history: lives alone in an apartment, employed as an accountant. Smokes 1 pack/day for 10-15 years. Occasional cannabis use (5mg/week). Denies other recreational drug use (cocaine, crystal meth, opioids, IV drugs). Consumes alcohol, 1-2 drinks/day, approximately 10 drinks/week. Reports trying to eat healthy for dinner, but eats out for most lunches. Exercises every other day, running for 30 minutes.
- Family history: father had a heart attack at 45 and cholesterol problems. Denies family history of stroke or cancer.

Physical Examination:
- Neck: swollen

Impression & Plan:
1. Chest pain
- Differential diagnosis: cardiac, pulmonary, musculoskeletal aetiologies.
- Investigations planned: ECG, chest X-ray, blood tests (cardiac enzymes, D-dimer if indicated).
- Treatment planned: Analgesia as needed.
- Relevant referrals: Consider cardiology referral depending on investigation results.

---

Patient Summary

- Topic/Issue #1: Sharp chest pain
  - Key takeaways or recommendations for this issue: Pain started last night, sharp, 7-8/10, left-sided. Worse with lying down and deep breaths, improved with not lying down. Associated with lightheadedness, trouble breathing, racing heart.
- Topic/Issue #2: Social history and family history of heart disease
  - Key takeaways or recommendations for this issue: Smokes 1 pack/day, occasional cannabis, 10 alcoholic drinks/week. Father had heart attack at 45 and cholesterol issues.

Key Takeaways
- Urgent investigation of chest pain.
- Cessation of smoking.
- Reduction of alcohol and cannabis use.
- Continue healthy diet and exercise.

Next Steps
- Follow up after investigations for review of results and further management.
- Seek immediate medical attention if chest pain worsens, new symptoms develop, or breathing difficulties increase significantly."""
    print(obj.summarize(content))
