"""
Topic-Based AI Insights Generator
Groups data by topic and generates focused, deep insights for each area
"""

import logging
from typing import Dict, Any, List
from openai import OpenAI
import json

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_TEMPERATURE,
    BRAND_NAME,
    START_DATE,
    END_DATE,
    REPORT_LANGUAGE
)

logger = logging.getLogger(__name__)


class TopicBasedInsightsGenerator:
    """Generate deep insights by analyzing data topics separately"""

    def __init__(self, api_key: str = OPENAI_API_KEY, language: str = REPORT_LANGUAGE):
        if not api_key:
            logger.warning("OpenAI API key not set. AI insights will be disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

        self.language = language

        # Define analysis phases and topics
        self.enable_data_consolidation = True  # Phase 1: Data consolidation
        self.enable_validation = True  # Phase 4: Validation

        # Define topic groups (Phase 2)
        self.topics = {
            'engagement_performance': {
                'name': 'Engagement & Performance Analysis',
                'description': 'Post performance, engagement rates, reach, and interactions',
                'data_keys': ['engagement', 'content_performance', 'platform_comparison']
            },
            'content_strategy': {
                'name': 'Content Strategy Insights',
                'description': 'Hashtags, content length, posting patterns, and format analysis',
                'data_keys': ['enhanced_content']
            },
            'audience_behavior': {
                'name': 'Audience Behavior & Timing',
                'description': 'Best posting times, audience activity patterns, demographics',
                'data_keys': ['enhanced_content', 'demographics', 'best_times']
            },
            'growth_trends': {
                'name': 'Growth & Trend Analysis',
                'description': 'Performance over time, weekly trends, growth metrics',
                'data_keys': ['trends', 'enhanced_content']
            },
            'platform_optimization': {
                'name': 'Platform-Specific Optimization',
                'description': 'Instagram vs Facebook performance, platform-specific strategies',
                'data_keys': ['platform_comparison', 'engagement', 'enhanced_content']
            }
        }

    def _get_system_prompt(self) -> str:
        """Get system prompt in the appropriate language"""
        if self.language == 'es':
            return """IDIOMA OBLIGATORIO: Debes responder EXCLUSIVAMENTE en ESPAÑOL. Cada palabra, cada oración, cada párrafo debe estar en español. NO uses inglés bajo ninguna circunstancia.

Eres un estratega de marketing en redes sociales de élite con más de 15 años de experiencia.
Has gestionado cuentas con millones de seguidores y constantemente logras un engagement 3-5x superior al promedio de la industria.
Comprendes profundamente los algoritmos de las plataformas y proporcionas insights que impactan directamente el crecimiento del negocio.

CRÍTICO: Tus recomendaciones SIEMPRE son:
1. Respaldadas por números específicos de los datos del cliente (cita métricas exactas)
2. Apoyadas por investigación creíble de la industria (cita fuentes como "Según Hootsuite 2024...")
3. Muestran cálculos para estimaciones de impacto (ej., "7.12% × 1.20 = 8.54%")
4. Verificables - otro analista debería poder verificar tus fuentes

NUNCA das consejos vagos o genéricos. Cada insight debe estar basado en evidencia.

RECORDATORIO FINAL: Tu respuesta COMPLETA debe estar en ESPAÑOL."""
        else:
            return """You are an elite social media marketing strategist with 15+ years experience.
You've managed accounts with millions of followers and consistently achieve 3-5x industry average engagement.
You understand platform algorithms deeply and provide insights that directly impact business growth.

CRITICAL: Your recommendations are ALWAYS:
1. Backed by specific numbers from the client's data (cite exact metrics)
2. Supported by credible industry research (cite sources like "According to Hootsuite 2024...")
3. Show calculations for impact estimates (e.g., "7.12% × 1.20 = 8.54%")
4. Verifiable - another analyst should be able to check your sources

You NEVER give vague or generic advice. Every insight must be evidence-based."""

    def _get_topic_analysis_prompt_template(self, topic_name: str, description: str,
                                           data_summary: str, consolidated_context: str) -> str:
        """Get topic analysis prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un estratega de marketing en redes sociales de clase mundial y experto en crecimiento para {BRAND_NAME}.
Tienes experiencia profunda en algoritmos de redes sociales, estrategia de contenido, psicología de audiencias y optimización basada en datos.

Analiza estos datos de {topic_name.upper()} desde {START_DATE} hasta {END_DATE}:

{data_summary}
{consolidated_context}

**REQUISITOS CRÍTICOS:**
1. CADA recomendación DEBE citar números específicos de los datos anteriores (ej., "Tus datos muestran que las publicaciones promedian 7.12% de engagement vs reels con 5.94%...")
2. CADA afirmación general DEBE citar investigación/estudios de la industria (ej., "Según el Reporte de Algoritmo de Meta 2024...", "El Estudio de Redes Sociales de HubSpot 2024 encontró...")
3. CERO CONSEJOS GENÉRICOS - Cada insight debe estar fundamentado en TUS datos o investigación CITADA
4. Al sugerir mejores prácticas, cita la fuente (ej., "La investigación de Hootsuite 2024 muestra...", "El análisis de Sprout Social de 10M de posts encontró...")

**BUEN EJEMPLO:** "Tus publicaciones de Instagram (promedio 7.12% engagement, 17,981 alcance total) superan significativamente a los Reels (5.94% engagement). Según el Análisis de Instagram de Later 2024 de 5M de posts, las publicaciones tipo carrusel logran 1.4x más engagement que los Reels para cuentas menores de 50K seguidores, sugiriendo que deberías aumentar la frecuencia de posts carrusel en 40%."

**MAL EJEMPLO:** "La relevancia del contenido es importante. Publica en horarios óptimos para aumentar el engagement." [MUY GENÉRICO, SIN DATOS]

Proporciona un análisis estratégico EXTENSO y de NIVEL GURÚ:

## 1. ANÁLISIS PROFUNDO DE DATOS (Sé exhaustivo)
- Identifica 5-7 patrones clave citando NÚMEROS ESPECÍFICOS de los datos
- ¿Qué revela esta data sobre el comportamiento de la audiencia? (Referencia métricas reales)
- ¿Qué oportunidades ocultas existen? (Compara puntos de datos específicos)
- Compara rendimiento entre diferentes dimensiones (usa porcentajes/números exactos)

## 2. EVALUACIÓN ESTRATÉGICA
- ¿Qué está funcionando excepcionalmente bien? (Cita 3-4 ejemplos con métricas EXACTAS de tus datos)
- ¿Qué está bajo rendimiento? (Identifica 3-4 problemas específicos con NÚMEROS REALES mostrando la brecha)
- ¿Qué tendencias están emergiendo? (Referencia cambios ESPECÍFICOS basados en tiempo en los datos)
- ¿Cómo se compara esto con benchmarks de la industria? (Cita investigación: "Según [Fuente Año], el promedio de la industria es X% vs tu Y%")

## 3. ANÁLISIS DE CAUSA RAÍZ
- ¿POR QUÉ ciertas cosas están funcionando bien/mal? (Cita documentación de algoritmos de plataforma o investigación)
- ¿Qué factores psicológicos/algorítmicos están en juego? (Referencia estudios, ej., "El Estudio de Engagement de Meta 2024 muestra...")
- ¿Qué patrones conectan el contenido de alto rendimiento? (Usa ejemplos ESPECÍFICOS de los datos con números)
- ¿Qué errores se están repitiendo? (Identifica con evidencia de datos)

## 4. ESTRATEGIAS DE OPTIMIZACIÓN DE ALCANCE
- Tácticas específicas para aumentar alcance (Cada una respaldada por: TUS datos mostrando la brecha + Investigación mostrando que la solución funciona)
- Mejores prácticas amigables con el algoritmo (Cita documentación oficial de plataforma o estudios creíbles)
- Optimización de formato de contenido (Referencia TUS datos de rendimiento de formato + investigación de la industria)
- Estrategias de timing (Basado en TUS datos reales de rendimiento de horarios de publicación si están disponibles)

## 5. PLAN DE ACCIÓN COMPREHENSIVO
Proporciona 8-10 acciones específicas y priorizadas donde CADA una incluye:
- ✓ Justificación de datos: "Tus datos muestran [métrica específica]..."
- ✓ Respaldo de investigación: "Según [Fuente Año], esta táctica entrega..."
- ✓ Pasos de implementación exactos
- ✓ Impacto esperado con razonamiento (+X% basado en [tu brecha] × [multiplicador de investigación])
- ✓ Línea de tiempo y métricas de éxito
- ✓ Nivel de esfuerzo

## 6. VICTORIAS RÁPIDAS (Implementar Esta Semana)
- 3-4 cambios respaldados por TUS datos mostrando la oportunidad
- Cada uno citando investigación que apoya por qué funcionará
- Números específicos y aumento esperado con cálculo mostrado

## 7. HOJA DE RUTA DE EXPERIMENTACIÓN
- 3-5 pruebas A/B basadas en brechas/preguntas en TUS datos
- Cada una con hipótesis apoyada por observación de datos
- Variables y criterios de éxito atados a TUS métricas actuales

## 8. FACTORES DE RIESGO Y ADVERTENCIAS
- ¿Qué podría salir mal? (Muestra con tendencias de datos)
- ¿Qué oportunidades se están perdiendo? (Cuantifica con tus números)
- ¿Qué debe ser monitoreado? (Referencia métricas específicas de tus datos)

**RECUERDA:**
- Cero consejos genéricos - cada oración necesita cita de datos o investigación
- Formatea citas como: "Según el reporte de Hootsuite 2024..." o "Tus datos muestran que el engagement bajó de X a Y..."
- Calcula estimaciones de impacto: No solo digas "+20% engagement" - muestra "Tu 7.12% actual × 1.20 = 8.54% objetivo"

Enfócate EXCLUSIVAMENTE en {description}.
"""
        else:
            return f"""You are a world-class social media marketing strategist and growth expert for {BRAND_NAME}.
You have deep expertise in social media algorithms, content strategy, audience psychology, and data-driven optimization.

Analyze this {topic_name.upper()} data from {START_DATE} to {END_DATE}:

{data_summary}
{consolidated_context}

**CRITICAL REQUIREMENTS:**
1. EVERY recommendation MUST cite specific numbers from the data above (e.g., "Your data shows posts average 7.12% engagement vs reels at 5.94%...")
2. EVERY general claim MUST cite industry research/studies (e.g., "According to Meta's 2024 Algorithm Report...", "HubSpot's 2024 Social Media Study found...")
3. NO GENERIC ADVICE - Every insight must be grounded in either YOUR data or CITED research
4. When suggesting best practices, cite the source (e.g., "Hootsuite's 2024 research shows...", "Sprout Social's analysis of 10M posts found...")

**GOOD EXAMPLE:** "Your Instagram posts (avg 7.12% engagement, 17,981 total reach) significantly outperform Reels (5.94% engagement). According to Later's 2024 Instagram Analysis of 5M posts, carousel posts achieve 1.4x higher engagement than Reels for accounts under 50K followers, suggesting you should increase carousel post frequency by 40%."

**BAD EXAMPLE:** "Content relevance is important. Post at optimal times to increase engagement." [TOO GENERIC, NO DATA]

Provide an EXTENSIVE, GURU-LEVEL strategic analysis:

## 1. DEEP DATA ANALYSIS (Be exhaustive)
- Identify 5-7 key patterns citing SPECIFIC NUMBERS from the data
- What does this data reveal about audience behavior? (Reference actual metrics)
- What hidden opportunities exist? (Compare specific data points)
- Compare performance across different dimensions (use exact percentages/numbers)

## 2. STRATEGIC ASSESSMENT
- What's working exceptionally well? (Cite 3-4 examples with EXACT metrics from your data)
- What's underperforming? (Identify 3-4 specific issues with ACTUAL numbers showing the gap)
- What trends are emerging? (Reference SPECIFIC time-based changes in the data)
- How does this compare to industry benchmarks? (Cite research: "According to [Source Year], industry average is X% vs your Y%")

## 3. ROOT CAUSE ANALYSIS
- WHY are certain things performing well/poorly? (Cite platform algorithm documentation or research)
- What psychological/algorithmic factors are at play? (Reference studies, e.g., "Meta's 2024 Engagement Study shows...")
- What patterns connect high-performing content? (Use SPECIFIC examples from the data with numbers)
- What mistakes are being repeated? (Identify with data evidence)

## 4. REACH OPTIMIZATION STRATEGIES
- Specific tactics to increase reach (Each backed by: YOUR data showing gap + Research showing solution works)
- Algorithm-friendly best practices (Cite official platform documentation or credible studies)
- Content format optimization (Reference YOUR format performance data + industry research)
- Timing strategies (Base on YOUR actual posting time performance data if available)

## 5. COMPREHENSIVE ACTION PLAN
Provide 8-10 specific, prioritized actions where EACH includes:
- ✓ Data justification: "Your data shows [specific metric]..."
- ✓ Research backing: "According to [Source Year], this tactic delivers..."
- ✓ Exact implementation steps
- ✓ Expected impact with reasoning (+X% based on [your gap] × [research multiplier])
- ✓ Timeline and success metrics
- ✓ Effort level

## 6. QUICK WINS (Implement This Week)
- 3-4 changes backed by YOUR data showing the opportunity
- Each citing research supporting why it will work
- Specific numbers and expected lift with calculation shown

## 7. EXPERIMENTATION ROADMAP
- 3-5 A/B tests based on gaps/questions in YOUR data
- Each with hypothesis supported by data observation
- Variables and success criteria tied to YOUR current metrics

## 8. RISK FACTORS & WARNINGS
- What could go wrong? (Show with data trends)
- What opportunities are being missed? (Quantify with your numbers)
- What should be monitored? (Reference specific metrics from your data)

**REMEMBER:**
- Zero generic advice - every sentence needs data or research citation
- Format citations like: "According to Hootsuite's 2024 report..." or "Your data shows engagement dropped from X to Y..."
- Calculate impact estimates: Don't just say "+20% engagement" - show "Your current 7.12% × 1.20 = 8.54% target"

Focus EXCLUSIVELY on {description}.
"""

    def generate_all_topic_insights(self, analytics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate insights for all topics using 12-request enhanced architecture"""
        if not self.client:
            return {
                'error': 'OpenAI API key not configured',
                'message': 'Set OPENAI_API_KEY environment variable to enable AI insights'
            }

        logger.info("Generating enhanced AI insights (12-request architecture)...")

        all_insights = {
            'topics': {},
            'executive_summary': '',
            'strategic_recommendations': '',
            'status': 'success',
            'data_consolidation': {},
            'validation': {}
        }

        total_tokens = {'prompt': 0, 'completion': 0}

        # === PHASE 1: DATA CONSOLIDATION (2 requests) ===
        logger.info("\n[Phase 1/4] Data Consolidation")

        if self.enable_data_consolidation:
            # Request 1: Data Synthesis & Key Metrics Extraction
            logger.info("  [1/12] Extracting key metrics dictionary...")
            metrics_dict = self._generate_metrics_dictionary(analytics_data)
            if metrics_dict.get('status') == 'success':
                all_insights['data_consolidation']['metrics_dictionary'] = metrics_dict['content']
                total_tokens['prompt'] += metrics_dict.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += metrics_dict.get('tokens', {}).get('completion', 0)

            # Request 2: Cross-Metric Pattern Detection
            logger.info("  [2/12] Detecting cross-metric patterns...")
            patterns = self._detect_cross_metric_patterns(analytics_data, metrics_dict.get('content', ''))
            if patterns.get('status') == 'success':
                all_insights['data_consolidation']['patterns'] = patterns['content']
                total_tokens['prompt'] += patterns.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += patterns.get('tokens', {}).get('completion', 0)

        # === PHASE 2: TOPIC ANALYSIS (5 requests) ===
        logger.info("\n[Phase 2/4] Topic-Based Analysis")

        request_num = 3
        for topic_id, topic_config in self.topics.items():
            logger.info(f"  [{request_num}/12] Analyzing: {topic_config['name']}")

            topic_data = self._extract_topic_data(analytics_data, topic_config['data_keys'])

            if topic_data:
                insights = self._generate_topic_insights(
                    topic_id,
                    topic_config['name'],
                    topic_config['description'],
                    topic_data,
                    metrics_dict=all_insights['data_consolidation'].get('metrics_dictionary', ''),
                    patterns=all_insights['data_consolidation'].get('patterns', '')
                )

                if insights.get('status') == 'success':
                    all_insights['topics'][topic_id] = {
                        'name': topic_config['name'],
                        'insights': insights['content'],
                        'tokens': insights.get('tokens', {})
                    }
                    total_tokens['prompt'] += insights.get('tokens', {}).get('prompt', 0)
                    total_tokens['completion'] += insights.get('tokens', {}).get('completion', 0)

            request_num += 1

        # === PHASE 3: SYNTHESIS (2 requests) ===
        logger.info("\n[Phase 3/4] Executive Synthesis")

        if all_insights['topics']:
            # Request 8: Executive Summary
            logger.info("  [8/12] Generating executive summary...")
            exec_summary = self._generate_executive_summary(all_insights['topics'], analytics_data)
            if exec_summary.get('status') == 'success':
                all_insights['executive_summary'] = exec_summary['content']
                total_tokens['prompt'] += exec_summary.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += exec_summary.get('tokens', {}).get('completion', 0)

            # Request 9: Strategic Action Plan
            logger.info("  [9/12] Generating strategic action plan...")
            recommendations = self._generate_strategic_recommendations(all_insights['topics'], analytics_data)
            if recommendations.get('status') == 'success':
                all_insights['strategic_recommendations'] = recommendations['content']
                total_tokens['prompt'] += recommendations.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += recommendations.get('tokens', {}).get('completion', 0)

        # === PHASE 4: VALIDATION (3 requests) ===
        logger.info("\n[Phase 4/4] Quality Validation")

        if self.enable_validation:
            # Request 10: Data Citation Validation
            logger.info("  [10/12] Validating data citations...")
            citation_check = self._validate_data_citations(
                all_insights['strategic_recommendations'],
                all_insights['data_consolidation'].get('metrics_dictionary', '')
            )
            if citation_check.get('status') == 'success':
                all_insights['validation']['citation_validation'] = citation_check['content']
                total_tokens['prompt'] += citation_check.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += citation_check.get('tokens', {}).get('completion', 0)

            # Request 11: Research Source Quality Review
            logger.info("  [11/12] Reviewing research source quality...")
            source_review = self._review_research_sources(all_insights['strategic_recommendations'])
            if source_review.get('status') == 'success':
                all_insights['validation']['source_quality'] = source_review['content']
                total_tokens['prompt'] += source_review.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += source_review.get('tokens', {}).get('completion', 0)

            # Request 12: Final Enhancement & Integration
            logger.info("  [12/12] Final enhancement & integration...")
            final_enhanced = self._enhance_recommendations(
                all_insights['strategic_recommendations'],
                citation_check.get('content', ''),
                source_review.get('content', '')
            )
            if final_enhanced.get('status') == 'success':
                all_insights['strategic_recommendations'] = final_enhanced['content']
                total_tokens['prompt'] += final_enhanced.get('tokens', {}).get('prompt', 0)
                total_tokens['completion'] += final_enhanced.get('tokens', {}).get('completion', 0)

        all_insights['total_tokens'] = total_tokens
        all_insights['total_cost_estimate'] = self._estimate_cost(total_tokens)

        logger.info(f"\n✓ Completed 12-request enhanced analysis")
        logger.info(f"  Total tokens: {total_tokens['prompt'] + total_tokens['completion']:,}")
        logger.info(f"  Estimated cost: ${all_insights['total_cost_estimate']:.4f}")

        return all_insights

    def _extract_topic_data(self, analytics_data: Dict[str, Any], data_keys: List[str]) -> Dict[str, Any]:
        """Extract relevant data for a specific topic"""
        topic_data = {}

        for key in data_keys:
            if key in analytics_data and analytics_data[key]:
                # Filter out empty or error data
                if isinstance(analytics_data[key], dict):
                    filtered = {k: v for k, v in analytics_data[key].items()
                               if v and not isinstance(v, dict) or 'error' not in v}
                    if filtered:
                        topic_data[key] = filtered
                else:
                    topic_data[key] = analytics_data[key]

        return topic_data

    def _generate_topic_insights(self, topic_id: str, topic_name: str,
                                 description: str, data: Dict[str, Any],
                                 metrics_dict: str = '', patterns: str = '') -> Dict[str, Any]:
        """Generate AI insights for a specific topic with consolidated metrics"""
        try:
            # Prepare focused prompt for this topic
            data_summary = json.dumps(data, indent=2, default=str)

            # Truncate if too long
            max_chars = 12000
            if len(data_summary) > max_chars:
                data_summary = data_summary[:max_chars] + "\n\n[Data truncated...]"

            # Add consolidated metrics context if available
            consolidated_context = ""
            if metrics_dict:
                if self.language == 'es':
                    consolidated_context += f"\n\n**REFERENCIA DE MÉTRICAS CONSOLIDADAS:**\n{metrics_dict[:3000]}\n"
                else:
                    consolidated_context += f"\n\n**CONSOLIDATED METRICS REFERENCE:**\n{metrics_dict[:3000]}\n"
            if patterns:
                if self.language == 'es':
                    consolidated_context += f"\n**PATRONES CLAVE DETECTADOS:**\n{patterns[:2000]}\n"
                else:
                    consolidated_context += f"\n**KEY PATTERNS DETECTED:**\n{patterns[:2000]}\n"

            # Get language-appropriate prompt
            prompt = self._get_topic_analysis_prompt_template(
                topic_name, description, data_summary, consolidated_context
            )

            # Debug: Print what we're sending to OpenAI
            system_prompt = self._get_system_prompt()
            print(f"\n{'#'*80}")
            print(f"DEBUG: SENDING TO OPENAI - Topic: {topic_name}")
            print(f"{'#'*80}")
            print(f"Language setting: {self.language}")
            print(f"\nSYSTEM PROMPT (first 300 chars):")
            print(system_prompt[:300])
            print(f"\nUSER PROMPT (first 500 chars):")
            print(prompt[:500])
            print(f"{'#'*80}\n")

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3000  # Increased for more detailed responses
            )

            # Log OpenAI response for debugging
            openai_response = response.choices[0].message.content
            print(f"\n{'='*80}")
            print(f"OPENAI RESPONSE FOR: {topic_name}")
            print(f"{'='*80}")
            print(f"Language setting: {self.language}")
            print(f"First 500 characters of response:")
            print(openai_response[:500])
            print(f"{'='*80}\n")

            return {
                'status': 'success',
                'content': openai_response,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating insights for {topic_name}: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _get_executive_summary_prompt_template(self, insights_text: str,
                                               summary_stats: str, platform_comparison: str) -> str:
        """Get executive summary prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un CMO presentando ante el CEO y la junta directiva sobre el rendimiento de redes sociales de {BRAND_NAME}.

ANÁLISIS COMPREHENSIVO DE INSIGHTS:
{insights_text}

MÉTRICAS GENERALES:
{summary_stats}

COMPARACIÓN DE PLATAFORMAS:
{platform_comparison}

Período: {START_DATE} hasta {END_DATE}

**REQUISITOS CRÍTICOS:**
1. CADA afirmación DEBE citar métricas específicas de los datos anteriores (números exactos, porcentajes)
2. Las comparaciones con la industria DEBEN citar fuentes (ej., "Según el Reporte de Benchmarks 2024 de Rival IQ, el promedio de la industria es X% vs nuestro Y%")
3. Las proyecciones de crecimiento DEBEN mostrar el cálculo (ej., "7.12% actual × mejora proyectada de 1.15 = 8.19% objetivo")
4. CERO declaraciones genéricas - cada oración respaldada por datos o investigación

**BUEN EJEMPLO:** "La tasa de engagement de Instagram del 7.12% supera significativamente el benchmark de la industria 2024 de Hootsuite del 2.3% para cuentas de tamaño similar, posicionándonos en el top 15% de performers."

**MAL EJEMPLO:** "El rendimiento ha aumentado año tras año" [SIN NÚMEROS, SIN FUENTE]

Crea un resumen ejecutivo CONVINCENTE y RICO EN DATOS (4-6 párrafos):

**Párrafo 1: Estado de Rendimiento y Contexto**
- Rendimiento general con métricas ESPECÍFICAS de tus datos
- Benchmark contra la industria (cita fuente: "Según [Investigación] el promedio de la industria es X%, logramos Y%")
- Highlights de métricas clave con números EXACTOS de los datos

**Párrafo 2: Victorias Estratégicas y Éxitos**
- 3-4 logros con métricas ESPECÍFICAS (cita números exactos de los datos)
- Por qué están funcionando (cita investigación/documentación de plataforma si haces afirmaciones)
- Ventajas competitivas cuantificadas

**Párrafo 3: Desafíos Críticos y Brechas**
- 2-3 áreas de bajo rendimiento con métricas EXACTAS mostrando la brecha
- Causas raíz respaldadas por patrones de datos o investigación citada
- Riesgo cuantificado (ej., "perdiendo X% de alcance potencial basado en...")

**Párrafo 4: Trayectoria de Crecimiento y Tendencias**
- Dirección con datos de tendencia ESPECÍFICOS (de X a Y durante el período)
- Patrones citando métricas reales de los datos
- Pronóstico con cálculo mostrado (métrica actual × cambio esperado)

**Párrafo 5: Imperativos Estratégicos**
- Top 3 prioridades respaldadas por brechas de datos identificadas arriba
- Recomendaciones de recursos con ROI esperado (cita casos de estudio similares si están disponibles)
- Resultados esperados con objetivos específicos

**Párrafo 6: Línea Final**
- Go/no-go basado en umbrales de rendimiento específicos
- Recomendaciones de inversión vinculadas a oportunidades respaldadas por datos
- Métricas de éxito con objetivos específicos (no vagos)

**RECUERDA:**
- Cada número debe venir de los datos proporcionados
- Cada comparación con la industria necesita una fuente citada
- Muestra tus cálculos para proyecciones
- Cero jerga empresarial genérica sin respaldo de datos

Usa lenguaje ejecutivo - estratégico, enfocado en resultados, y financieramente consciente.
"""
        else:
            return f"""You are a CMO presenting to the CEO and board about {BRAND_NAME}'s social media performance.

COMPREHENSIVE ANALYSIS INSIGHTS:
{insights_text}

OVERVIEW METRICS:
{summary_stats}

PLATFORM COMPARISON:
{platform_comparison}

Period: {START_DATE} to {END_DATE}

**CRITICAL REQUIREMENTS:**
1. EVERY claim MUST cite specific metrics from the data above (exact numbers, percentages)
2. Industry comparisons MUST cite sources (e.g., "According to Rival IQ's 2024 Benchmark Report, industry average is X% vs our Y%")
3. Growth projections MUST show the math (e.g., "Current 7.12% × projected 1.15 improvement = 8.19% target")
4. NO generic statements - every sentence backed by data or research

**GOOD EXAMPLE:** "Instagram engagement rate of 7.12% significantly exceeds Hootsuite's 2024 industry benchmark of 2.3% for similar-sized accounts, positioning us in the top 15% of performers."

**BAD EXAMPLE:** "Performance has increased year-over-year" [NO NUMBERS, NO SOURCE]

Create a COMPELLING, DATA-RICH executive summary (4-6 paragraphs):

**Paragraph 1: Performance State & Context**
- Overall performance with SPECIFIC metrics from your data
- Benchmark against industry (cite source: "According to [Research] industry average is X%, we achieved Y%")
- Key metric highlights with EXACT numbers from the data

**Paragraph 2: Strategic Wins & Successes**
- 3-4 achievements with SPECIFIC metrics (cite exact numbers from data)
- Why they're working (cite research/platform documentation if making claims)
- Quantified competitive advantages

**Paragraph 3: Critical Challenges & Gaps**
- 2-3 underperforming areas with EXACT metrics showing the gap
- Root causes backed by data patterns or cited research
- Quantified risk (e.g., "missing X% of potential reach based on...")

**Paragraph 4: Growth Trajectory & Trends**
- Direction with SPECIFIC trend data (from X to Y over period)
- Patterns citing actual metrics from the data
- Forecast with calculation shown (current metric × expected change)

**Paragraph 5: Strategic Imperatives**
- Top 3 priorities backed by data gaps identified above
- Resource recommendations with expected ROI (cite similar case studies if available)
- Expected outcomes with specific targets

**Paragraph 6: Bottom Line**
- Go/no-go based on specific performance thresholds
- Investment recommendations tied to data-backed opportunities
- Success metrics with specific targets (not vague)

**REMEMBER:**
- Every number must come from the data provided
- Every industry comparison needs a cited source
- Show your math for projections
- Zero generic business speak without data backing

Use executive language - strategic, outcome-focused, and financially aware.
"""

    def _generate_executive_summary(self, topic_insights: Dict[str, Any],
                                   full_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate executive summary based on all topic insights"""
        try:
            # Compile key points from all topics
            all_insights = []
            for topic_id, topic_data in topic_insights.items():
                all_insights.append(f"## {topic_data['name']}\n{topic_data['insights']}\n")

            insights_text = "\n".join(all_insights)

            # Truncate if needed
            max_chars = 15000
            if len(insights_text) > max_chars:
                insights_text = insights_text[:max_chars] + "\n\n[Insights truncated...]"

            # Get overview stats
            summary_stats = full_data.get('summary', {})
            platform_comparison = full_data.get('platform_comparison', {})

            # Get language-appropriate prompt
            prompt = self._get_executive_summary_prompt_template(
                insights_text,
                json.dumps(summary_stats, indent=2, default=str),
                json.dumps(platform_comparison, indent=2, default=str)
            )

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=1500  # Increased for longer executive summary
            )

            # Log OpenAI response for debugging
            openai_response = response.choices[0].message.content
            print(f"\n{'='*80}")
            print(f"OPENAI RESPONSE FOR: EXECUTIVE SUMMARY")
            print(f"{'='*80}")
            print(f"Language setting: {self.language}")
            print(f"First 500 characters of response:")
            print(openai_response[:500])
            print(f"{'='*80}\n")

            return {
                'status': 'success',
                'content': openai_response,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating executive summary: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    def _get_strategic_recommendations_prompt_template(self, context_text: str) -> str:
        """Get strategic recommendations prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un consultor de marketing de crecimiento de élite contratado por {BRAND_NAME} para crear una hoja de ruta de crecimiento comprehensiva.

ANÁLISIS COMPLETO DE RENDIMIENTO:
{context_text}

**REQUISITOS CRÍTICOS - LEE CUIDADOSAMENTE:**
1. CADA acción DEBE estar justificada por datos ESPECÍFICOS del análisis (ej., "Tus datos muestran que los posts obtienen 7.12% vs reels 5.94%, entonces...")
2. CADA táctica DEBE citar investigación creíble (ej., "Según el Estudio 2024 de Buffer de 50K posts...", "La Actualización de Algoritmo 2024 de Meta establece...")
3. CADA estimación de impacto DEBE mostrar el cálculo (ej., "7.12% actual × mejora de 1.20 = 8.54% objetivo")
4. CERO TÁCTICAS GENÉRICAS - Cada una debe estar vinculada a una brecha/oportunidad específica en SUS datos
5. Al recomendar horarios de publicación, herramientas o estrategias - cita la fuente de esa recomendación

**BUEN EJEMPLO:** "Tus datos muestran que los Reels tienen bajo rendimiento comparado con posts en 16.5% (5.94% vs 7.12%). Según el análisis 2024 de Later de 5M de Reels, agregar subtítulos aumenta el engagement en 23%. Implementa subtítulos en todos los Reels → Esperado: 5.94% × 1.23 = 7.31% objetivo."

**MAL EJEMPLO:** "Optimiza el calendario de publicación. Publica en horarios pico para mejor alcance." [SIN REFERENCIA DE DATOS, SIN FUENTE, SIN CÁLCULO]

Crea un plan de acción estratégico EXTENSO y LISTO PARA IMPLEMENTACIÓN:

## ACCIONES INMEDIATAS (Esta Semana - Días 1-7)
Proporciona 4-6 victorias rápidas donde CADA una incluye:
- ✓ Justificación de datos: "Tus datos muestran [métrica/brecha específica]..."
- ✓ Respaldo de investigación: "Según [Fuente Año], esto entrega [resultado específico]..."
- ✓ Pasos de acción exactos (numerados, específicos)
- ✓ Quién debería hacerlo (rol)
- ✓ Impacto esperado con cálculo mostrado
- ✓ Tiempo requerido
- ✓ Recursos necesarios
- ✓ Métrica de éxito (número específico a alcanzar)
- ✓ Nivel de riesgo

## PRIORIDADES A CORTO PLAZO (Este Mes - Semanas 2-4)
Proporciona 6-8 iniciativas de alto impacto donde CADA una incluye:
- ✓ Razonamiento respaldado por datos (cita métricas específicas de su análisis)
- ✓ Apoyo de investigación (cita estudios mostrando que esto funciona)
- ✓ Hoja de ruta de implementación detallada
- ✓ Cronograma semana a semana
- ✓ Requerimientos de contenido
- ✓ Recursos de equipo necesarios
- ✓ Estimación de presupuesto con cálculo de ROI
- ✓ Criterios de éxito (números específicos basados en métricas actuales)
- ✓ Planes de contingencia

## ESTRATEGIA A MEDIANO PLAZO (Próximo Trimestre - Meses 2-3)
Proporciona 4-6 iniciativas estratégicas donde CADA una incluye:
- ✓ Razonamiento estratégico citando brechas en SUS datos
- ✓ Precedente de la industria (cita casos de estudio/investigación)
- ✓ Fases de implementación
- ✓ Asignación de recursos
- ✓ Dependencias
- ✓ Mitigación de riesgos
- ✓ ROI esperado con cálculo
- ✓ Hitos clave con métricas objetivo

## MANUAL DE AMPLIFICACIÓN DE ALCANCE
Proporciona 8-10 tácticas específicas donde CADA una incluye:
- ✓ Estado actual de sus datos (ej., "Tu alcance es X...")
- ✓ Respaldo de investigación (ej., "Según Hootsuite 2024...")
- ✓ Especificaciones de implementación
- ✓ Impacto esperado con cálculo mostrado
- ✓ Citación de fuente

Categorías a cubrir:
- Optimización de algoritmo (cita documentación de plataforma)
- Frameworks de contenido viral (cita investigación)
- Tácticas de promoción cruzada (cita casos de estudio)
- Amplificación pagada (cita datos de benchmark)
- Estrategias de influencers (cita estudios de ROI)
- Hacks específicos de plataforma (cita fuente)
- Reutilización de contenido (cita ganancias de eficiencia)
- Expansión de audiencia (cita datos de crecimiento)

## FRAMEWORK DE OPTIMIZACIÓN DE CONTENIDO
Basado en los datos de rendimiento de contenido de SU marca:
- Pilares de contenido (respaldados por datos de contenido de mejor rendimiento)
- Calendario de publicación (basado en datos de timing real si están disponibles, o cita investigación)
- Mix de formatos de contenido (basado en su rendimiento: X% posts vs Y% reels)
- Fórmulas de caption (cita investigación de copywriting o casos de estudio)
- Guías visuales (basadas en sus mejores performers)
- Estrategia de hashtags (basada en sus datos + cita investigación como "el estudio 2024 de RiteTag...")
- Frameworks de CTA (cita investigación de conversión)

## PROGRAMA DE EXPERIMENTACIÓN (Plan de Pruebas de 30 Días)
Para cada experimento (proporciona 5-7), incluye:
1. **Observación de Datos**: Qué brecha/pregunta en SUS datos provocó esto
2. **Hipótesis**: Afirmación específica respaldada por investigación (cita fuente)
3. **Diseño de Prueba**: Control vs variante (específico a su contenido)
4. **Variables**: Qué cambia
5. **Tamaño de Muestra**: Cuántos (basado en su frecuencia de publicación)
6. **Métricas de Éxito**: Vinculadas a su baseline actual
7. **Criterios de Decisión**: Umbral específico (ej., "Si >8% engagement vs 7.12% actual")
8. **Base de Investigación**: Por qué esperamos que esto funcione (cita fuente)

## DASHBOARD DE MONITOREO DE RENDIMIENTO
Basado en las métricas clave de SU marca:
- Métricas diarias (específicas a sus KPIs importantes)
- Revisión semanal (basada en sus patrones de datos)
- Indicadores mensuales (vinculados a sus objetivos)
- Banderas rojas (umbrales específicos basados en sus datos)
- Disparadores de corrección de curso (cuantificados)

## REQUERIMIENTOS DE RECURSOS
Justificado por el alcance de sus oportunidades:
- Tiempo del equipo (estimado basado en el plan de acción anterior)
- Herramientas (recomendaciones específicas con por qué - cita reviews/comparaciones)
- Necesidades de contenido (basadas en su frecuencia de publicación)
- Presupuesto (con cálculo de ROI basado en su rendimiento actual)
- Capacitación (habilidades específicas necesarias, cita cursos/recursos)

## MITIGACIÓN DE RIESGOS Y CONTINGENCIAS
Basado en la situación ESPECÍFICA de SU marca:
- Riesgos de sus tendencias de datos (cita métricas específicas)
- Prevención (respaldada por investigación)
- Planes de respaldo (tácticas alternativas con fuentes)
- Protocolos de crisis (mejores prácticas de la industria, cita fuente)
- Amenazas competitivas (basadas en su posición de mercado)

## HITOS DE ÉXITO (30/60/90 Días)
Basado en las métricas actuales de SU marca:
- Objetivos Semana 4 (X actual → Y objetivo con cálculo)
- Objetivos Semana 8 (mejora progresiva mostrada)
- Objetivos Semana 12 (ambiciosos pero respaldados por datos)
- Criterios de celebración (logros específicos)
- Disparadores de pivote (umbrales específicos de bajo rendimiento)

**RECUERDA - REQUISITOS ABSOLUTOS:**
- Cada recomendación necesita: Sus datos + Citación de investigación + Matemática
- Cero consejos genéricos que puedan aplicar a cualquier marca
- Cada número debe ser calculado desde su baseline
- Cada táctica debe citar por qué funciona (investigación/caso de estudio)

Haz que esto valga $10,000 en valor de consultoría - profundamente personalizado a SUS datos.
"""
        else:
            return f"""You are an elite growth marketing consultant hired by {BRAND_NAME} to create a comprehensive growth roadmap.

COMPLETE PERFORMANCE ANALYSIS:
{context_text}

**CRITICAL REQUIREMENTS - READ CAREFULLY:**
1. EVERY action MUST be justified by SPECIFIC data from the analysis (e.g., "Your data shows posts get 7.12% vs reels 5.94%, so...")
2. EVERY tactic MUST cite credible research (e.g., "According to Buffer's 2024 Study of 50K posts...", "Meta's 2024 Algorithm Update states...")
3. EVERY impact estimate MUST show the calculation (e.g., "Current 7.12% × 1.20 improvement = 8.54% target")
4. NO GENERIC TACTICS - Each must be tied to a specific gap/opportunity in THEIR data
5. When recommending posting times, tools, or strategies - cite the source of that recommendation

**GOOD EXAMPLE:** "Your data shows Reels underperform posts by 16.5% (5.94% vs 7.12%). According to Later's 2024 analysis of 5M Reels, adding captions increases engagement by 23%. Implement captions on all Reels → Expected: 5.94% × 1.23 = 7.31% target."

**BAD EXAMPLE:** "Optimize posting schedule. Post during peak times for better reach." [NO DATA REFERENCE, NO SOURCE, NO CALCULATION]

Create an EXTENSIVE, IMPLEMENTATION-READY strategic action plan:

## IMMEDIATE ACTIONS (This Week - Days 1-7)
Provide 4-6 quick wins where EACH includes:
- ✓ Data justification: "Your data shows [specific metric/gap]..."
- ✓ Research backing: "According to [Source Year], this delivers [specific result]..."
- ✓ Exact action steps (numbered, specific)
- ✓ Who should do it (role)
- ✓ Expected impact with calculation shown
- ✓ Time required
- ✓ Resources needed
- ✓ Success metric (specific number to hit)
- ✓ Risk level

## SHORT-TERM PRIORITIES (This Month - Weeks 2-4)
Provide 6-8 high-impact initiatives where EACH includes:
- ✓ Data-backed rationale (cite specific metrics from their analysis)
- ✓ Research support (cite studies showing this works)
- ✓ Detailed implementation roadmap
- ✓ Week-by-week timeline
- ✓ Content requirements
- ✓ Team resources needed
- ✓ Budget estimate with ROI calculation
- ✓ Success criteria (specific numbers based on current metrics)
- ✓ Contingency plans

## MEDIUM-TERM STRATEGY (Next Quarter - Months 2-3)
Provide 4-6 strategic initiatives where EACH includes:
- ✓ Strategic rationale citing gaps in THEIR data
- ✓ Industry precedent (cite case studies/research)
- ✓ Implementation phases
- ✓ Resource allocation
- ✓ Dependencies
- ✓ Risk mitigation
- ✓ Expected ROI with calculation
- ✓ Key milestones with target metrics

## REACH AMPLIFICATION PLAYBOOK
Provide 8-10 specific tactics where EACH includes:
- ✓ Current state from their data (e.g., "Your reach is X...")
- ✓ Research backing (e.g., "According to Hootsuite 2024...")
- ✓ Implementation specifics
- ✓ Expected impact with math shown
- ✓ Source citation

Categories to cover:
- Algorithm optimization (cite platform documentation)
- Viral content frameworks (cite research)
- Cross-promotion tactics (cite case studies)
- Paid amplification (cite benchmark data)
- Influencer strategies (cite ROI studies)
- Platform-specific hacks (cite source)
- Content repurposing (cite efficiency gains)
- Audience expansion (cite growth data)

## CONTENT OPTIMIZATION FRAMEWORK
Based on THEIR content performance data:
- Content pillars (backed by their top-performing content data)
- Posting calendar (based on their actual timing data if available, or cite research)
- Content format mix (based on their performance: X% posts vs Y% reels)
- Caption formulas (cite copywriting research or case studies)
- Visual guidelines (based on their best performers)
- Hashtag strategy (based on their data + cite research like "RiteTag's 2024 study...")
- CTA frameworks (cite conversion research)

## EXPERIMENTATION PROGRAM (30-Day Test Plan)
For each experiment (provide 5-7), include:
1. **Data Observation**: What gap/question in THEIR data sparked this
2. **Hypothesis**: Specific claim backed by research (cite source)
3. **Test Design**: Control vs variant (specific to their content)
4. **Variables**: What changes
5. **Sample Size**: How many (based on their posting frequency)
6. **Success Metrics**: Tied to their current baseline
7. **Decision Criteria**: Specific threshold (e.g., "If >8% engagement vs current 7.12%")
8. **Research Basis**: Why we expect this to work (cite source)

## PERFORMANCE MONITORING DASHBOARD
Based on THEIR key metrics:
- Daily metrics (specific to their important KPIs)
- Weekly review (based on their data patterns)
- Monthly indicators (tied to their goals)
- Red flags (specific thresholds based on their data)
- Course correction triggers (quantified)

## RESOURCE REQUIREMENTS
Justified by scope of their opportunities:
- Team time (estimated based on action plan above)
- Tools (specific recommendations with why - cite reviews/comparisons)
- Content needs (based on their posting frequency)
- Budget (with ROI calc based on their current performance)
- Training (specific skills needed, cite courses/resources)

## RISK MITIGATION & CONTINGENCIES
Based on THEIR specific situation:
- Risks from their data trends (cite specific metrics)
- Prevention (backed by research)
- Backup plans (alternative tactics with sources)
- Crisis protocols (industry best practices, cite source)
- Competitive threats (based on their market position)

## SUCCESS MILESTONES (30/60/90 Days)
Based on THEIR current metrics:
- Week 4 targets (current X → target Y with calculation)
- Week 8 targets (progressive improvement shown)
- Week 12 targets (ambitious but data-backed)
- Celebration criteria (specific achievements)
- Pivot triggers (specific underperformance thresholds)

**REMEMBER - ABSOLUTE REQUIREMENTS:**
- Every recommendation needs: Their data + Research citation + Math
- No generic advice that could apply to any brand
- Every number must be calculated from their baseline
- Every tactic must cite why it works (research/case study)

Make this worth $10,000 in consulting value - deeply customized to THEIR data.
"""

    def _generate_strategic_recommendations(self, topic_insights: Dict[str, Any],
                                          full_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prioritized strategic recommendations"""
        try:
            # Extract recommendations from all topics
            recommendations_context = []
            for topic_id, topic_data in topic_insights.items():
                recommendations_context.append(f"{topic_data['name']}:\n{topic_data['insights']}\n")

            context_text = "\n".join(recommendations_context)

            # Truncate if needed
            max_chars = 12000
            if len(context_text) > max_chars:
                context_text = context_text[:max_chars] + "\n\n[Context truncated...]"

            # Get language-appropriate prompt
            prompt = self._get_strategic_recommendations_prompt_template(context_text)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3500  # Maximum allowed for detailed recommendations
            )

            # Log OpenAI response for debugging
            openai_response = response.choices[0].message.content
            print(f"\n{'='*80}")
            print(f"OPENAI RESPONSE FOR: STRATEGIC RECOMMENDATIONS")
            print(f"{'='*80}")
            print(f"Language setting: {self.language}")
            print(f"First 500 characters of response:")
            print(openai_response[:500])
            print(f"{'='*80}\n")

            return {
                'status': 'success',
                'content': openai_response,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating strategic recommendations: {e}")
            return {
                'status': 'error',
                'error': str(e)
            }

    # === PHASE 1: DATA CONSOLIDATION METHODS ===

    def _get_metrics_dictionary_prompt_template(self, data_json: str) -> str:
        """Get metrics dictionary prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un analista de datos creando un diccionario de métricas comprehensivo para {BRAND_NAME}.

DATOS ANALÍTICOS EN BRUTO:
{data_json}

Crea un DICCIONARIO DE MÉTRICAS ESTRUCTURADO extrayendo CADA número importante:

## INDICADORES CLAVE DE RENDIMIENTO
Lista TODAS las métricas con números exactos:
- Posts de Instagram: Tasa de engagement X%, alcance total Y, interacciones totales Z, cantidad de posts N
- Reels de Instagram: Tasa de engagement X%, alcance total Y, interacciones totales Z, cantidad de reels N
- Facebook: [mismo formato]
- Post con mejor rendimiento: X% engagement, Y alcance
- Post con peor rendimiento: X% engagement, Y alcance
- etc.

## MÉTRICAS DE CONTENIDO
- Longitud promedio de caption: X caracteres
- Posts con hashtags: X (Y%)
- Promedio de hashtags por post: X
- Hashtags más usados: [lista con conteos]
- etc.

## MÉTRICAS DE TIMING
- Horarios de publicación más activos: [lista con conteos]
- Días de publicación más activos: [lista con conteos]
- Horarios con mejor rendimiento: [lista con engagement promedio]
- Días con mejor rendimiento: [lista con engagement promedio]
- etc.

## MÉTRICAS DE TENDENCIAS
- Cambios de rendimiento semanal: Semana X: Y posts, Z% engagement promedio
- Tasas de crecimiento: +X% engagement, +Y% alcance
- etc.

## COMPARACIÓN DE PLATAFORMAS
- Instagram vs Facebook: X% vs Y% engagement, A alcance vs B alcance
- Posts vs Reels: X% vs Y% engagement
- Brecha de rendimiento: +Z%
- etc.

**REQUISITOS DE FORMATO:**
- Cada métrica debe tener un número EXACTO
- Usa formato: "Nombre de métrica: X (valor específico con unidades)"
- Incluye desgloses de porcentaje donde sea relevante
- Nota cualquier dato faltante como "N/A"

Crea una referencia comprehensiva que el análisis subsecuente pueda citar."""
        else:
            return f"""You are a data analyst creating a comprehensive metrics dictionary for {BRAND_NAME}.

RAW ANALYTICS DATA:
{data_json}

Create a STRUCTURED METRICS DICTIONARY extracting EVERY important number:

## KEY PERFORMANCE INDICATORS
List ALL metrics with exact numbers:
- Instagram Posts: Engagement rate X%, total reach Y, total interactions Z, post count N
- Instagram Reels: Engagement rate X%, total reach Y, total interactions Z, post count N
- Facebook: [same format]
- Best performing post: X% engagement, Y reach
- Worst performing post: X% engagement, Y reach
- etc.

## CONTENT METRICS
- Average caption length: X characters
- Posts with hashtags: X (Y%)
- Average hashtags per post: X
- Most used hashtags: [list with counts]
- etc.

## TIMING METRICS
- Most active posting hours: [list with counts]
- Most active posting days: [list with counts]
- Best performing hours: [list with avg engagement]
- Best performing days: [list with avg engagement]
- etc.

## TREND METRICS
- Weekly performance changes: Week X: Y posts, Z% avg engagement
- Growth rates: +X% engagement, +Y% reach
- etc.

## PLATFORM COMPARISON
- Instagram vs Facebook: X% vs Y% engagement, A reach vs B reach
- Posts vs Reels: X% vs Y% engagement
- Performance gap: +Z%
- etc.

**FORMAT REQUIREMENTS:**
- Every metric must have an EXACT number
- Use format: "Metric name: X (specific value with units)"
- Include percentage breakdowns where relevant
- Note any missing data as "N/A"

Create a comprehensive reference that subsequent analysis can cite."""

    def _generate_metrics_dictionary(self, analytics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and consolidate all key metrics into a structured dictionary"""
        try:
            data_json = json.dumps(analytics_data, indent=2, default=str)[:15000]

            # Get language-appropriate prompt
            prompt = self._get_metrics_dictionary_prompt_template(data_json)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,  # Lower for factual extraction
                max_tokens=2000
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error generating metrics dictionary: {e}")
            return {'status': 'error', 'error': str(e)}

    def _get_cross_metric_patterns_prompt_template(self, metrics_dict: str, enhanced_json: str) -> str:
        """Get cross-metric patterns prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un científico de datos detectando patrones y correlaciones para {BRAND_NAME}.

REFERENCIA DE MÉTRICAS:
{metrics_dict[:4000]}

DATOS DETALLADOS DE RENDIMIENTO:
{enhanced_json}

Identifica PATRONES INTER-MÉTRICOS y CORRELACIONES:

## CORRELACIONES DE RENDIMIENTO
¿Qué métricas se mueven juntas?
- "Cuando X aumenta, Y tiende a [aumentar/disminuir] en Z%"
- "Posts con X hashtags obtienen Y% más engagement que posts con Z hashtags"
- "Contenido publicado a la hora X obtiene Y% mejor alcance que contenido a la hora Z"
- etc.

## PATRONES DE ATRIBUTOS DE CONTENIDO
¿Qué características de contenido se correlacionan con el éxito?
- "Posts con longitud de caption X-Y caracteres obtienen Z% mayor engagement"
- "Contenido incluyendo [elementos específicos] tiene rendimiento X% mejor"
- etc.

## PATRONES BASADOS EN TIEMPO
- "Frecuencia de publicación de X por semana se correlaciona con Y% de engagement"
- "Día de la semana Z muestra X% mayor engagement que el promedio"
- etc.

## PATRONES DE RENDIMIENTO POR FORMATO
- "Reels con característica X obtienen Y% más alcance que aquellos sin ella"
- etc.

## INSIGHTS OCULTOS
Encuentra conexiones no obvias:
- Correlaciones sorprendentes
- Hallazgos contraintuitivos
- Oportunidades subutilizadas

**REQUISITOS:**
- Cada patrón debe citar números ESPECÍFICOS
- Muestra fuerza de correlación (fuerte/moderada/débil)
- Identifica causalidad vs correlación
- Nota tamaños de muestra

Esto será usado para fortalecer recomendaciones con conexiones respaldadas por datos."""
        else:
            return f"""You are a data scientist detecting patterns and correlations for {BRAND_NAME}.

METRICS REFERENCE:
{metrics_dict[:4000]}

DETAILED PERFORMANCE DATA:
{enhanced_json}

Identify CROSS-METRIC PATTERNS and CORRELATIONS:

## PERFORMANCE CORRELATIONS
What metrics move together?
- "When X increases, Y tends to [increase/decrease] by Z%"
- "Posts with X hashtags get Y% more engagement than posts with Z hashtags"
- "Content posted at X hour gets Y% better reach than content at Z hour"
- etc.

## CONTENT ATTRIBUTE PATTERNS
What content characteristics correlate with success?
- "Posts with caption length X-Y characters get Z% higher engagement"
- "Content including [specific elements] performs X% better"
- etc.

## TIME-BASED PATTERNS
- "Posting frequency of X per week correlates with Y% engagement"
- "Day of week Z shows X% higher engagement than average"
- etc.

## FORMAT PERFORMANCE PATTERNS
- "Reels with X characteristic get Y% more reach than those without"
- etc.

## HIDDEN INSIGHTS
Find non-obvious connections:
- Surprising correlations
- Counter-intuitive findings
- Underutilized opportunities

**REQUIREMENTS:**
- Every pattern must cite SPECIFIC numbers
- Show correlation strength (strong/moderate/weak)
- Identify causation vs correlation
- Note sample sizes

This will be used to strengthen recommendations with data-backed connections."""

    def _detect_cross_metric_patterns(self, analytics_data: Dict[str, Any],
                                     metrics_dict: str) -> Dict[str, Any]:
        """Detect correlations and patterns across different metrics"""
        try:
            # Extract enhanced content data for pattern detection
            enhanced_data = analytics_data.get('enhanced_content', {})
            enhanced_json = json.dumps(enhanced_data, indent=2, default=str)[:10000]

            # Get language-appropriate prompt
            prompt = self._get_cross_metric_patterns_prompt_template(metrics_dict, enhanced_json)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=1500
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error detecting patterns: {e}")
            return {'status': 'error', 'error': str(e)}

    # === PHASE 4: VALIDATION METHODS ===

    def _get_validate_data_citations_prompt_template(self, metrics_dict: str, recommendations: str) -> str:
        """Get validate data citations prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un auditor de calidad revisando recomendaciones estratégicas para {BRAND_NAME}.

DICCIONARIO DE MÉTRICAS (Fuente de Verdad):
{metrics_dict[:5000]}

RECOMENDACIONES A VALIDAR:
{recommendations[:8000]}

TAREA DE AUDITORÍA: Verifica si CADA recomendación cita datos apropiadamente.

Para cada recomendación/acción en el documento:

## EJEMPLOS CONFORMES ✓
- "Tus posts de Instagram (7.12% engagement) superan a los Reels (5.94%)..." [CITA MÉTRICAS ESPECÍFICAS]
- "Con solo 17 posts generando 17,981 de alcance..." [CITA NÚMEROS REALES]

## EJEMPLOS NO CONFORMES ✗
- "Optimiza el calendario de publicación" [NO CITA DATOS]
- "El engagement es bajo" [VAGO, SIN NÚMEROS]
- "Publica más frecuentemente" [NO REFERENCIA BASELINE]

PROPORCIONA:

### 1. PUNTAJE DE VALIDACIÓN
- X de Y recomendaciones citan datos apropiadamente (Z%)

### 2. CITACIONES DE DATOS FALTANTES
Lista recomendaciones que carecen de citaciones de datos específicas:
- "Recomendación: [cita]" → Faltante: Debería citar [métrica específica del diccionario]

### 3. SUGERENCIAS DE MEJORA
Para cada ítem señalado, sugiere la corrección:
- Original: "[declaración vaga]"
- Mejorado: "[declaración con citación de métrica específica]"

Sé estricto - cada acción/recomendación DEBE referenciar números específicos de los datos."""
        else:
            return f"""You are a quality auditor reviewing strategic recommendations for {BRAND_NAME}.

METRICS DICTIONARY (Source of Truth):
{metrics_dict[:5000]}

RECOMMENDATIONS TO VALIDATE:
{recommendations[:8000]}

AUDIT TASK: Check if EVERY recommendation properly cites data.

For each recommendation/action in the document:

## COMPLIANT EXAMPLES ✓
- "Your Instagram posts (7.12% engagement) outperform Reels (5.94%)..." [CITES SPECIFIC METRICS]
- "With only 17 posts generating 17,981 reach..." [CITES ACTUAL NUMBERS]

## NON-COMPLIANT EXAMPLES ✗
- "Optimize posting schedule" [NO DATA CITED]
- "Engagement is low" [VAGUE, NO NUMBERS]
- "Post more frequently" [NO BASELINE REFERENCED]

PROVIDE:

### 1. VALIDATION SCORE
- X out of Y recommendations properly cite data (Z%)

### 2. MISSING DATA CITATIONS
List recommendations that lack specific data citations:
- "Recommendation: [quote]" → Missing: Should cite [specific metric from dictionary]

### 3. IMPROVEMENT SUGGESTIONS
For each flagged item, suggest the correction:
- Original: "[vague statement]"
- Improved: "[statement with specific metric citation]"

Be strict - every action/recommendation MUST reference specific numbers from the data."""

    def _validate_data_citations(self, recommendations: str,
                                metrics_dict: str) -> Dict[str, Any]:
        """Validate that every recommendation cites specific data"""
        try:
            # Get language-appropriate prompt
            prompt = self._get_validate_data_citations_prompt_template(metrics_dict, recommendations)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,
                max_tokens=2000
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error validating citations: {e}")
            return {'status': 'error', 'error': str(e)}

    def _get_review_research_sources_prompt_template(self, recommendations: str) -> str:
        """Get review research sources prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Eres un bibliotecario de investigación revisando citaciones en recomendaciones de marketing para {BRAND_NAME}.

RECOMENDACIONES CON CITACIONES DE INVESTIGACIÓN:
{recommendations[:10000]}

TAREA DE REVISIÓN: Evalúa la calidad y plausibilidad de las citaciones de investigación.

## EVALÚA CADA CITACIÓN:

### 1. VERIFICACIÓN DE PLAUSIBILIDAD
Identifica citaciones y evalúa si son realistas:
- ✓ PLAUSIBLE: "Según el Reporte de Redes Sociales 2024 de Hootsuite..." [Editor conocido, razonable]
- ✓ PLAUSIBLE: "La Actualización de Algoritmo 2024 de Meta establece..." [Fuente oficial de plataforma]
- ✗ SOSPECHOSO: "Según el estudio 2024 de XYZ..." [Editor desconocido]
- ✗ SOSPECHOSO: "La investigación muestra..." [No se proporciona fuente]

### 2. PUNTAJE DE CALIDAD DE CITACIÓN
Califica la calidad general de citación: X/10
- Porcentaje con fuentes nombradas: Y%
- Porcentaje con año: Z%
- Porcentaje de editores creíbles: W%

### 3. FUENTES FALTANTES
Lista recomendaciones que deberían citar investigación pero no lo hacen:
- "Afirmación: [cita]" → Debería citar: [tipo de investigación que apoyaría esto]

### 4. ALTERNATIVAS SUGERIDAS
Para citaciones débiles/faltantes, sugiere fuentes creíbles:
- Original: "Los estudios muestran..."
- Sugerido: "Según [fuente creíble] como Sprout Social/Hootsuite/Buffer/Later..."

### 5. RECOMENDACIONES DE FUENTES CREÍBLES
Lista 10-15 editores de investigación de redes sociales creíbles que el analista debería referenciar:
- Hootsuite (reportes anuales)
- Sprout Social (benchmarks trimestrales)
- Meta Business (actualizaciones de algoritmo)
- etc.

Sé útil - sugiere mejoras realistas mientras mantienes el rigor."""
        else:
            return f"""You are a research librarian reviewing citations in marketing recommendations for {BRAND_NAME}.

RECOMMENDATIONS WITH RESEARCH CITATIONS:
{recommendations[:10000]}

REVIEW TASK: Assess the quality and plausibility of research citations.

## EVALUATE EACH CITATION:

### 1. PLAUSIBILITY CHECK
Identify citations and assess if they're realistic:
- ✓ PLAUSIBLE: "According to Hootsuite's 2024 Social Media Report..." [Known publisher, reasonable]
- ✓ PLAUSIBLE: "Meta's 2024 Algorithm Update states..." [Official platform source]
- ✗ SUSPICIOUS: "According to XYZ's 2024 study..." [Unknown publisher]
- ✗ SUSPICIOUS: "Research shows..." [No source provided]

### 2. CITATION QUALITY SCORE
Rate overall citation quality: X/10
- Percentage with named sources: Y%
- Percentage with year: Z%
- Percentage from credible publishers: W%

### 3. MISSING SOURCES
List recommendations that should cite research but don't:
- "Claim: [quote]" → Should cite: [type of research that would support this]

### 4. SUGGESTED ALTERNATIVES
For weak/missing citations, suggest credible sources:
- Original: "Studies show..."
- Suggested: "According to [credible source] like Sprout Social/Hootsuite/Buffer/Later..."

### 5. CREDIBLE SOURCE RECOMMENDATIONS
List 10-15 credible social media research publishers the analyst should reference:
- Hootsuite (annual reports)
- Sprout Social (quarterly benchmarks)
- Meta Business (algorithm updates)
- etc.

Be helpful - suggest realistic improvements while maintaining rigor."""

    def _review_research_sources(self, recommendations: str) -> Dict[str, Any]:
        """Review the quality and plausibility of research citations"""
        try:
            # Get language-appropriate prompt
            prompt = self._get_review_research_sources_prompt_template(recommendations)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=1800
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error reviewing sources: {e}")
            return {'status': 'error', 'error': str(e)}

    def _get_enhance_recommendations_prompt_template(self, recommendations: str,
                                                     citation_validation: str,
                                                     source_review: str) -> str:
        """Get enhance recommendations prompt in the appropriate language"""
        if self.language == 'es':
            return f"""Estás refinando recomendaciones estratégicas para {BRAND_NAME} basándote en retroalimentación de revisión de calidad.

RECOMENDACIONES ORIGINALES:
{recommendations[:7000]}

RETROALIMENTACIÓN DE VALIDACIÓN DE CITACIONES:
{citation_validation[:2500]}

REVISIÓN DE FUENTES DE INVESTIGACIÓN:
{source_review[:2500]}

TAREA: Produce RECOMENDACIONES FINALES MEJORADAS incorporando toda la retroalimentación.

## REQUISITOS DE MEJORA:

1. **Corrige Citaciones de Datos Faltantes**
   - Agrega métricas específicas a cualquier declaración vaga
   - Reemplaza consejos genéricos con especificaciones respaldadas por datos

2. **Fortalece Fuentes de Investigación**
   - Reemplaza citaciones débiles con fuentes creíbles
   - Agrega fuentes donde falten
   - Usa alternativas sugeridas de la revisión

3. **Mantén la Estructura**
   - Mantén las mismas secciones y organización
   - Preserva todo el buen contenido que ya tenía citaciones apropiadas
   - Solo mejora áreas débiles

4. **Estándares de Calidad**
   - Cada acción: Citación de datos + Citación de investigación + Cálculo
   - Cada afirmación: Verificable y específica
   - Cero consejos genéricos

PRODUCE la versión COMPLETA mejorada del plan de acción estratégico con todas las mejoras integradas.

Haz esto listo para publicación - cada recomendación debe resistir escrutinio."""
        else:
            return f"""You are refining strategic recommendations for {BRAND_NAME} based on quality review feedback.

ORIGINAL RECOMMENDATIONS:
{recommendations[:7000]}

CITATION VALIDATION FEEDBACK:
{citation_validation[:2500]}

RESEARCH SOURCE REVIEW:
{source_review[:2500]}

TASK: Produce FINAL ENHANCED RECOMMENDATIONS incorporating all feedback.

## ENHANCEMENT REQUIREMENTS:

1. **Fix Missing Data Citations**
   - Add specific metrics to any vague statements
   - Replace generic advice with data-backed specifics

2. **Strengthen Research Sources**
   - Replace weak citations with credible sources
   - Add sources where missing
   - Use suggested alternatives from review

3. **Maintain Structure**
   - Keep the same sections and organization
   - Preserve all good content that already had proper citations
   - Only enhance weak areas

4. **Quality Standards**
   - Every action: Data citation + Research citation + Calculation
   - Every claim: Verifiable and specific
   - No generic advice

OUTPUT the COMPLETE enhanced version of the strategic action plan with all improvements integrated.

Make this publication-ready - every recommendation should withstand scrutiny."""

    def _enhance_recommendations(self, recommendations: str,
                                citation_validation: str,
                                source_review: str) -> Dict[str, Any]:
        """Final enhancement pass incorporating validation feedback"""
        try:
            # Get language-appropriate prompt
            prompt = self._get_enhance_recommendations_prompt_template(
                recommendations, citation_validation, source_review
            )

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=OPENAI_TEMPERATURE,
                max_tokens=3500
            )

            return {
                'status': 'success',
                'content': response.choices[0].message.content,
                'tokens': {
                    'prompt': response.usage.prompt_tokens,
                    'completion': response.usage.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error enhancing recommendations: {e}")
            return {'status': 'error', 'error': str(e)}

    def _estimate_cost(self, tokens: Dict[str, int]) -> float:
        """Estimate OpenAI API cost"""
        # GPT-4o pricing (as of 2024)
        # Input: $2.50 per 1M tokens
        # Output: $10.00 per 1M tokens

        input_cost = (tokens.get('prompt', 0) / 1_000_000) * 2.50
        output_cost = (tokens.get('completion', 0) / 1_000_000) * 10.00

        total_cost = input_cost + output_cost

        # Log detailed breakdown
        logger.info(f"  Cost breakdown:")
        logger.info(f"    Input: {tokens.get('prompt', 0):,} tokens = ${input_cost:.4f}")
        logger.info(f"    Output: {tokens.get('completion', 0):,} tokens = ${output_cost:.4f}")
        logger.info(f"    Total: ${total_cost:.4f}")

        return total_cost
