def match_skills(resume_skills, jd_skills):
    resume_set = set([s.lower() for s in resume_skills])
    jd_set = set([s.lower() for s in jd_skills])
    matches = resume_set.intersection(jd_set)
    match_score = len(matches) / len(jd_set) if len(jd_set) > 0 else 0
    return {
        "matched_skills": list(matches),
        "missing_skills": list(jd_set - resume_set),
        "match_percentage": round(match_score * 100, 2)
    }
