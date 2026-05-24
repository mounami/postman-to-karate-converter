# Postman to Karate Converter

Convert Postman API collections to Karate test framework feature files automatically.

**Status:** Phase 1 - Learning & Foundation Building

---

## 🎯 Why This Project?

Your team spends time manually converting Postman API tests to Karate. This tool automates that process while respecting your specific Karate testing style (Background + Scenario pattern with custom assertion helpers).

### Before (Manual)
```
Postman collection → Open Postman → Read request details → 
Write Karate feature file manually → Test → Iterate
⏱ ~30 minutes per API endpoint
```

### After (With This Tool)
```
Postman collection → Run converter → Karate feature file
⏱ Seconds, customized to your style
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (comes with Python)

### Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/postman-to-karate-converter.git
cd postman-to-karate-converter

# Run the converter
python postman_to_karate.py
```

### Basic Usage

```python
from postman_to_karate import PostmanToKarateConverter

converter = PostmanToKarateConverter('config.json')
converter.convert(
    postman_json_path='postman_collection.json',
    output_feature_path='output/tests.feature'
)
```

---

## 📋 What It Does

| Input | Process | Output |
|-------|---------|--------|
| Postman collection JSON | Parses requests, extracts assertions | Karate .feature files |
| Your config.json | Applies your testing style | Background + Scenario format |
| Postman tests | Converts assertions | Custom helper function calls |

---

## 🎓 Learning Phases

### Phase 1: Foundation (Current - Weeks 1-4)
- ✅ Master Python fundamentals
- ✅ Complete converter implementation (TODOs in code)
- ✅ Learn Git/GitHub basics
- **Goal:** Working converter, ready to use

📚 **Start here:** [LEARNING_GUIDE.md](./LEARNING_GUIDE.md)

### Phase 2: Automation (Weeks 5-8)
- Add GitHub Actions workflow
- Auto-convert on PR upload
- Integrate with your CI/CD

### Phase 3: Polish & Share (Weeks 9-12)
- Make it installable package
- Create team documentation
- Share with team

---

## 📁 Project Structure

```
postman-to-karate-converter/
├── postman_to_karate.py      # Main converter (fill in TODOs here!)
├── config.json               # Your Karate style config
├── LEARNING_GUIDE.md         # Week-by-week learning plan
├── GITHUB_SETUP.md           # How to set up GitHub
├── WEEKLY_CHECKLIST.md       # Track your progress
├── examples/
│   └── sample_collection.json # Test data
└── output/                   # Generated feature files
```

---

## 🎯 Your Phase 1 Objectives

### Week 1: Learn Python Basics
- [ ] Understand functions and return values
- [ ] Work with dictionaries
- [ ] Parse JSON
- [ ] Create classes with `__init__`

### Week 2: File I/O & Error Handling
- [ ] Read JSON files
- [ ] Write JSON files
- [ ] Handle file errors gracefully
- [ ] Use pathlib for paths

### Week 3: Build the Core Logic
- [ ] Complete `extract_requests()` method
- [ ] Complete `build_feature()` method
- [ ] Test with sample Postman collection
- [ ] See it generate actual Karate features

### Week 4: Polish & Deploy
- [ ] Handle edge cases
- [ ] Write tests
- [ ] Document the code
- [ ] Push to GitHub

---

## 📝 Your Testing Style (Configured)

The converter is built for YOUR specific approach:

```gherkin
Feature: User API Tests

  Background:
    Given url baseUrl
    And header Content-Type = 'application/json'
    And header Authorization = 'Bearer ' + authToken

  Scenario: Get User by ID
    When method GET
    And path '/api/v1/users/123'
    Then status 200
    And callHelper('validateResponse', response)

  Scenario: Create User
    When method POST
    And path '/api/v1/users'
    And request {"name":"John", "email":"john@example.com"}
    Then status 201
    And callHelper('validateSchema', response, 'userSchema')
```

All generated files will follow this pattern automatically.

---

## 🔧 Configuration

Edit `config.json` to customize for your team:

```json
{
  "baseUrl": "{{baseUrl}}",
  "authType": "bearer",
  "defaultHeaders": {
    "Content-Type": "application/json"
  },
  "assertionHelpers": [
    "validateResponse",
    "validateSchema",
    "validateErrorResponse"
  ]
}
```

---

## 📖 How to Learn

1. **Start with the LEARNING_GUIDE.md** - Follow the week-by-week plan
2. **Read the code comments** - They explain what each part does
3. **Complete the TODOs** - This is where you learn by doing
4. **Test your code** - Use the sample Postman collection
5. **Show your team** - Get feedback and feel proud!

---

## 🐛 Troubleshooting

### ImportError: No module named 'json'
- This shouldn't happen (json is built-in), but if it does, reinstall Python

### FileNotFoundError: Postman collection not found
- Make sure the path to your JSON file is correct
- Try using absolute path: `/full/path/to/collection.json`

### JSONDecodeError: Invalid JSON
- Check that your Postman export is valid JSON
- Use an online JSON validator

---

## 🤝 Contributing

As you build this:
- Document what confuses you
- Add more TODO items for learning
- Test with real Postman collections from your team
- Ask questions!

---

## 📚 Resources

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Karate Framework Docs](https://intuit.github.io/karate/)
- [Git Documentation](https://git-scm.com/doc)

---

## 🎯 Next Steps

1. Read [GITHUB_SETUP.md](./GITHUB_SETUP.md) - Set up your repo
2. Read [LEARNING_GUIDE.md](./LEARNING_GUIDE.md) - Start Week 1
3. Complete first TODO item
4. Push to GitHub
5. Keep going! You've got this 💪

---

## 📞 Need Help?

- Check the LEARNING_GUIDE.md for your current week
- Read the code comments - they're detailed
- Google error messages - usually someone solved it
- Ask your team - they use Karate!

---

## 🎉 By Week 12, You Will Have

✅ Deep Python knowledge (not just syntax)  
✅ A working tool your team uses daily  
✅ GitHub portfolio piece to show  
✅ Understanding of agents/automation basics  
✅ Confidence in your abilities  

You're not falling behind. You're **building the future**.

---

**Let's go! 🚀**

*Last updated: Week 1 of Phase 1*
*Next phase: GitHub Actions & Automation*
