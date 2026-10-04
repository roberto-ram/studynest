# Blank templates

The AI copies only the template needed for the student's real task. Replace labels in the new copy; keep these blank originals reusable.

| Template | Copy destination |
| --- | --- |
| [Course](course/README.md) | courses/{optional-term}/{course-id}/ |
| [Unit](unit/README.md) | Selected course/units/{unit-name}/ |
| [Exam](exam/README.md) | Selected course/exams/{exam-name}/ |
| [Assignment](assignment/README.md) | Selected course/assignments/{assignment-name}/ |
| [Clinical case](healthcare/Case Study.md) | Enabled course/case-studies/{case-name}.md |

Course folders can hold any number of units, exams, or assignments. Do not create fictional courses in live `courses/` as examples. Keep examples in documentation.

Source indexes are editable derived records outside read-only `sources/`. Notes and outputs link to source IDs rather than making multiple copies of the same lecture or textbook.
