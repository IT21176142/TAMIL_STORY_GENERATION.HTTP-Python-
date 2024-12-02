def story_generation_tamil_prompt(converted_text):
  story_generate_prompting = [
                {
                    "role": "system",
                    "content": "Extract Details from medical report"
                },
                {"role": "user", "content": f"கதையின் பெயர்: {converted_text}"}
  ]
  return story_generate_prompting







